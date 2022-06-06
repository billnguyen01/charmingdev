# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_res_partner(models.Model):
    _inherit = 'res.partner'
    customer_no = fields.Char('Customer Number')
    name_chinese = fields.Char('Chinese Name')
    name_english = fields.Char('English Name')
    address_chinese = fields.Text('Chinese Address')
    address_english = fields.Text('English Address')
    fax = fields.Char('Fax')
    attention = fields.Char('Attention')
    invattn = fields.Char('Invoice Attention')
    contact = fields.Char('Contact')
    paydesc = fields.Text('Payment Description')
    remark = fields.Text('Remark')
    monthpay = fields.Char('Month pay')
    currency = fields.Many2one("res.currency", string="Currency")
    crlimit = fields.Boolean("Credit Limited", default=False)
    crlimit_amount = fields.Integer('Credit Limit Amount')
    discnt = fields.Char('Discount')
    sales_code = fields.Char('Sales Code')
    invdiscnt = fields.Char('Invoice Discount')
    chiadd = fields.Char('Chiadd')
    allow_payment = fields.Char('Allow Payment')
    auto_open_inv_ers_inv = fields.Selection([('openInvoice', 'Open Invoice'),
                                              ('ersInvoice', 'ERS Invoice')],
                                             string="Auto Open Invoice/ERS Invoice")
    payment_type = fields.Selection([('bank', 'Bank'), ('creditCard', 'Credit Card'),
                                     ('cash', 'Cash')], string="Payment Type")
    lang_use = fields.Selection([('english', 'E'), ('chinese', 'C')], string="Language")
    payterm = fields.Selection([('0', '0'), ('7', '7'),
                                ('15', '15'), ('20', '20'),
                                ('30', '30'), ('45', '45'),
                                ('60', '60'), ('90', '90')], string="Payterm")





