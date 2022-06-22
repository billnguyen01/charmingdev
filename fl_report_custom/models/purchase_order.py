# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_cost = fields.Float(string='Delivery Cost', digits='Product Price')
