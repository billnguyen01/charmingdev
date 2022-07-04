# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MRPRoutingWorkCenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    is_subcontract = fields.Boolean(string='Subcontract?', default=False)
    sub_bom_id = fields.Many2one('mrp.bom', string='Bill Of Material')
    supplier = fields.Many2one('res.partner', string='Supplier')
    product_service = fields.Many2one('product.template', string='Product')
    cost_per_unit = fields.Float(string='Cost Per Unit')
