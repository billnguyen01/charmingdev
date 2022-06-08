# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_sale_order(models.Model):
    _inherit = 'sale.order'
    paid = fields.Float('Paid', compute="depends_invoice_id")
    remaining = fields.Integer('Remaining')
    payment_schedule = fields.Selection([('late', 'Late'), ('not_late', 'Not late')], string="Payment Schedule")
    can_deliver = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Can deliver")
    count_paid = fields.Many2many("account.move", string='Count Paid')

    @api.depends('invoice_ids')
    def depends_invoice_id(self):
        for invoice in self:
            amount_due = 0.0
            if invoice:
                for aml in invoice.invoice_ids:
                    amount_due += (aml.amount_total - aml.amount_residual)
            invoice.update({
                'paid': amount_due
            })


class warning_delivery(models.Model):
    _inherit = 'stock.picking'
    delivery_warning = fields.Boolean('Delivery Warning', compute="compute_delivery_warning")

    def compute_delivery_warning(self):
        for record in self:
            record['delivery_warning'] = record.sale_id.is_warning







