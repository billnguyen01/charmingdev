from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_no = fields.Char(string='Product No')
    material_no = fields.Char(string='Customer Material No')
