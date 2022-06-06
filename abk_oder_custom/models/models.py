# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_sale_order(models.Model):
    _inherit = 'sale.order'
    # paid = fields.Integer('Paid')
    # remaining = fields.Integer('Remaining')
    # payment_schedule = fields.Selection([('late', 'Late'), ('not_late', 'Not late')], string="Payment Schedule")
    # can_deliver = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Can deliver")





