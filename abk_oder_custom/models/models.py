# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_sale_order(models.Model):
    _inherit = 'sale.order'
    paid = fields.Float('Paid', compute="depends_invoice_id")
    remaining = fields.Integer('Remaining')
    payment_schedule = fields.Selection([('late', 'Late'), ('not_late', 'Not late')], string="Payment Schedule")
    can_deliver = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Can deliver")
    count_paid = fields.Many2many("account.move", string='Count Paid')

    abk_purchase_order_number = fields.Integer('Purchase Order Number')
    abk_purchase_order_date = fields.Datetime('Purchase Order Date')
    abk_customer_id = fields.Char('CustomerID')
    abk_customer_name = fields.Char('Customer Name')
    abk_customer_purchase_order = fields.Char('Customer Purchase Order')
    abk_sales_code = fields.Char('Sales Code')
    abk_payment_description = fields.Text('Payment Description')
    abk_attention = fields.Char('Attention')
    abk_currency = fields.Char('Currency')
    abk_symbol = fields.Char('Symbol')
    abk_rate = fields.Char('Rate')
    abk_amount = fields.Float('Amount')
    abk_hk_amount = fields.Float('HKAmount')
    abk_remark = fields.Char('Remark')
    abk_user_id = fields.Char('User ID')
    abk_creation_date = fields.Datetime('Creation Date')
    abk_amendement_user = fields.Char('Amendement User')
    abk_amendement_date = fields.Datetime('Amendement Date')
    abk_amendement_time = fields.Float('Amendement Time')
    abk_po_void = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="PO Void")
    abk_con_status = fields.Char('Con Status')
    abk_sales_date = fields.Datetime('Sales Date')
    abk_salesperson = fields.Char('Salesperson')
    abk_salesperson_name = fields.Char('Salesperson name')
    abk_sales_team = fields.Char('Sales team')
    abk_sales_order_type = fields.Char('Sales Order Type')
    abk_sales_order_number = fields.Integer('Sales Order number')
    abk_project = fields.Char('Project')
    abk_product_number = fields.Integer('Product number')
    abk_product_description = fields.Text('Product description')
    abk_material_type = fields.Char('Material Type')
    abk_group = fields.Char('Group')
    abk_customer_material_number = fields.Integer('Customer Material Number')
    abk_order_quantity = fields.Integer('Order Quantity')
    abk_output_quantity = fields.Integer('Output Quantity')
    abk_unit = fields.Integer('Unit')
    abk_order_currency = fields.Char('Order Currency')
    abk_require_date = fields.Datetime('Require date')
    abk_delivery_address = fields.Char('Delivery address')
    abk_delivery_description = fields.Text('Delivery Description')
    abk_item_size = fields.Text('Item size')
    abk_proforma_invoice_remark = fields.Char('Proforma Invoice Remark')
    abk_co_remark = fields.Char('CO Remark')
    abk_customer_remark = fields.Char('Customer Remark')
    abk_created_by = fields.Char('Created by')
    abk_po_number = fields.Char('PO number')
    abk_status = fields.Char('Status')
    abk_direct_manufacturing = fields.Char('Direct manufacturing')
    abk_outsourcing = fields.Char('Outsourcing')
    abk_brand = fields.Char('Brand')
    abk_product_importance = fields.Char('Product importance')
    abk_customer_number = fields.Char('Customer number')
    abk_po_project = fields.Char('PO project')
    abk_delivery_date = fields.Datetime('Delivery date')
    abk_price_list = fields.Float('Price list')
    abk_ft = fields.Float('FT(USD)?')
    abk_ct = fields.Float('CT(USD)?')
    abk_customer_short_form = fields.Char('Customer short form')
    abk_sub_brand = fields.Char('Sub-Brand')
    abk_salesman = fields.Char('Salesman')
    abk_sortkey1 = fields.Char('Sortkey1')
    abk_hkd_amount = fields.Integer('HKD Amount (After exchange)')
    abk_agent = fields.Char('Agent')
    abk_web_order_number = fields.Integer('Web Order Number')
    abk_web_order_line_item = fields.Char('Web Order Line Item')
    abk_art_work_number_of_page = fields.Integer('Art Work Number of Page')
    abk_art_work_size = fields.Char('Art Work Size')
    abk_format_id = fields.Integer('Format ID')
    abk_customer_service_person = fields.Char('Customer Service Person')
    abk_referrer = fields.Char('Referrer')
    abk_proforma_invoice_number = fields.Integer('Proforma Invoice Number')
    abk_podate = fields.Datetime('Po Date')
    abk_custpono = fields.Char('Customer Po Number')
    abk_input_date_time = fields.Datetime('Input Date')
    abk_conprn = fields.Char('Con Prn')
    abk_condate_time = fields.Datetime('Con Date')
    abk_ename = fields.Char('English Name')


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







