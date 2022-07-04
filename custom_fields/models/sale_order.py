from odoo import api, fields, models
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_name_english = fields.Char(string='Customer English Name')
    customer_id = fields.Char(string='Customer ID')
    customer_short = fields.Char(string='Customer Short Name')
    created_by = fields.Many2one('res.users', string="Created By")
    product_importance = fields.Char(string='Product Importance')
    customer_number = fields.Char(string='Customer No')
    po_number = fields.Char(string='PO Number')
    salesman = fields.Char(string='Sales Man')
    sort_key = fields.Char(string='Sort Key')
    format_id = fields.Integer(string='Format ID')
    order_currency = fields.Char(string='Order Currency')
    customer_service = fields.Char(string='Customer Service Person')
    sale_ids = fields.Many2many('sale.order', 'sale_order_reference_rel', 'sale_id', 'ref_id',
                                string="Previous Sale")
    sales_code = fields.Text(string='Sales Code')
    attention = fields.Many2one('res.partner', 'Attention')
    remark = fields.Text(string='Remark')
    sales_date = fields.Date(string='Sales Date')
    project = fields.Text(string='Project')
    web_order_no = fields.Integer(string='Web Order No')
    agent = fields.Char(string='Agent')
    brand = fields.Char(string='Brand')
    sub_brand = fields.Char(string='Sub Brand')
    delivery_date = fields.Date(string='Delivery Date')
    po_project = fields.Char(string='PO Project')
    status = fields.Char(string='Status')
    po_valid = fields.Boolean(string='PO Valid')
    customer_remark = fields.Text(string='Customer Remark')
    co_mark = fields.Char(string='CO Mark')
    delivery_address = fields.Text(string='Delivery Address')
    delivery_descr = fields.Text(string='Delivery Description')
    require_date = fields.Date(string="Require Date")
    sale_type = fields.Char(string="Sale Order Type")
    payment_description = fields.Char(string='Payment Description')
    creation_date = fields.Datetime(string="Created Date", default=datetime.today())
    amendment_user = fields.Many2one('res.users', string="Last Updated By")
    amendment_date = fields.Datetime(string='Last Updated Date')
    proforma_number = fields.Char(string="Proforma Invoice Number")
    referrer = fields.Char(string="Referrer")
    proforma_remark = fields.Char(string="Proforma Invoice Remark")
    po_order = fields.Many2many('purchase.order', string="PO Order")

    @api.onchange('partner_id')
    def _onchange_sale_order(self):
        for rec in self:
            self.sale_ids = self.search([('partner_id', '=', rec.partner_id.id), ('state', '!=', ['draft', 'sent'])])

    @api.onchange('partner_id')
    def _onchange_customer_purchase(self):
        for rec in self:
            customer = self.env['res.partner'].search([('id', '=', rec.partner_id.id)])
            self.customer_name_english = customer.name_english
            self.customer_number = customer.customer_no
            self.customer_id = customer.id
            self.po_order = self.env['purchase.order'].search([('partner_id', '=', rec.partner_id.id)])

    @api.model
    def create(self, vals):
        print(vals['created_by'])
        vals['created_by'] = self.env.user.id
        return super(SaleOrder, self).create(vals)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_no = fields.Char(related='product_id.product_no')
    group = fields.Char(string='Group')
    unit = fields.Integer(string='Units')
    item_size = fields.Char(string='Item Size')
    direct_manufacture = fields.Char(string='Dir.Manufacture')
    outsourcing = fields.Char(string='Outsourcing')
    hka_amount = fields.Float(string='HKA Amount')
    currency = fields.Text(string="Currency")
    symbol = fields.Text(string="Symbol")
    rate = fields.Float(string="Rate")
    amount = fields.Float(string="Amount")
    material_type = fields.Char(string="Material Type")
    output_quantity = fields.Integer(string='Output Quantity')
    ft = fields.Char(string='FT(USD)')
    ct = fields.Char(string='CT(USD)')
    hkd_amount = fields.Float(string='Amount(HKD)')
    web_line_item = fields.Char(string='Web Order Line Item')
    art_work_no_pages = fields.Char(string='Art Work Pages')
    art_work_size = fields.Char(string='Art Work Size')
    customer_material_no = fields.Char(related='product_id.material_no')
