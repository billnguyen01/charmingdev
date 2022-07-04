# -*- coding: utf-8 -*-

from odoo import models, fields, api

import time
import logging

_logger = logging.getLogger(__name__)


class MrpWorkOrderSubcontract(models.Model):
    _inherit = 'mrp.workorder'

    is_subcontract = fields.Boolean(compute='_compute_is_subcontract', string="Subcontract?", store=False)
    sub_bom_id = fields.Many2one('mrp.bom', string='Bill Of Material', store=False, compute='_compute_sub_bom')

    @api.depends('operation_id')
    def _compute_is_subcontract(self):
        for record in self:
            record['is_subcontract'] = record.operation_id.is_subcontract

    @api.depends('operation_id')
    def _compute_sub_bom(self):
        for record in self:
            record['sub_bom_id'] = record.operation_id.sub_bom_id

    def button_subcontract(self):
        self.create_po()
        self.create_transfer_go()
        self.create_transfer_arrive()

    def create_po(self):
        self.env['purchase.order'].create({
            "partner_id": self.operation_id.supplier.id,
            'order_line': [(0, 0, {
                'name': self.operation_id.product_service.name,
                'product_id': self.operation_id.product_service.id,
                'product_qty': self.production_id.product_qty,
                'product_uom': self.product_uom_id.id,
                'price_unit': self.operation_id.cost_per_unit,
                'date_planned': time.strftime('%Y-%m-%d'),
            })],
        })

    def create_transfer_go(self):
        operation = self.operation_id
        production = self.production_id

        move_lines = []
        for item in production.workorder_ids:
            move_lines.append((0, 0, {
                'name': item.product_id.name,
                'product_id': item.product_id.id,
                'product_uom_qty': item.qty_produced,
                'product_uom': item.product_id.uom_id.id,
                'location_id': production.location_src_id.id,
                'location_dest_id': production.location_dest_id.id
            }))

        picking = self.env['stock.picking'].create({
            'location_id': production.location_src_id.id,
            'location_dest_id': production.location_dest_id.id,
            'partner_id': operation.supplier.id,
            'picking_type_id': self.env.ref('stock.picking_type_out').id,
            'move_lines': move_lines
        })

        picking.action_confirm()

    def create_transfer_arrive(self):
        operation = self.operation_id
        production = self.production_id

        picking = self.env['stock.picking'].create({
            'location_id': production.location_dest_id.id,
            'location_dest_id': production.location_src_id.id,
            'partner_id': operation.supplier.id,
            'picking_type_id': self.env.ref('stock.picking_type_in').id,
            'move_lines': [(0, 0, {
                'name': self.product_id.name,
                'product_id': self.product_id.id,
                'product_uom_qty': self.qty_produced,
                'product_uom': self.product_id.uom_id.id,
                'location_id': production.location_dest_id.id,
                'location_dest_id': production.location_src_id.id
            })]
        })

        picking.action_confirm()
