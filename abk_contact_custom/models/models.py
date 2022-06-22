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

    abk_short_char01 = fields.Char('ShortChar01')
    abk_check_box06 = fields.Boolean('CheckBox06')
    abk_sales_rep_code = fields.Char('SalesRepCode')
    abk_character01 = fields.Char('Character01')
    abk_character02 = fields.Char('Character02')
    abk_character03 = fields.Char('Character03')
    abk_comment = fields.Text('Comment')
    abk_currency_code = fields.Char('CurrencyCode')
    abk_est_date = fields.Char('EstDate')
    abk_terms_code = fields.Char('TermsCode')
    abk_discount_percent = fields.Char('DiscountPercent')
    abk_tax_region_code = fields.Char('TaxRegionCode')
    abk_resale_id = fields.Char('ResaleID')
    abk_consolidate_so = fields.Char('ConsolidateSO')
    abk_one_invper_ps = fields.Char('OneInvPerPS')
    abk_ers_order = fields.Char('ERSOrder')
    abk_allow_alt_bill_to = fields.Char('AllowAltBillTo')
    abk_list_code = fields.Char('ListCode')
    abk_credit_hold = fields.Char('CreditHold')
    abk_tot_invoice_credit = fields.Char('TotInvoiceCredit')
    abk_tot_order_credit = fields.Char('TotOrderCredit')
    abk_tot_open_credit = fields.Char('TotOpenCredit')
    abk_bt_cust_id = fields.Char('BTCustID')
    abk_default_bill_to = fields.Char('DefaultBillTo')
    abk_gl_control_type = fields.Char('GLControlType')
    abk_gl_control_code = fields.Char('GLControlCode')
    abk_per_con_name = fields.Char('PerConName')
    abk_ship_to_num = fields.Char('ShipToNum')
    abk_phone_num = fields.Char('PhoneNum')
    abk_fax_num = fields.Char('FaxNum')
    abk_primary_ship_to = fields.Char('PrimaryShipTo')








