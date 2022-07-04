from odoo import models, fields, api


class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order'

    abk_productno = fields.Char('Product Number')
    abk_podate = fields.Datetime('Order Date', default=fields.Datetime.now)
    abk_custno = fields.Char('Customer Number')
    abk_salescode = fields.Char('Sales Code')
    abk_pono = fields.Char('Order Number')
    abk_expdeldate = fields.Datetime('Expected delivery date')
    abk_otcharge = fields.Char('Over Time Charge')
    abk_process = fields.Char('Process')
    abk_yard = fields.Char('Yard')
    abk_content = fields.Char('Content')
    abk_productype = fields.Char('Material Type')
    abk_brand = fields.Char('Brand')
    abk_remark2 = fields.Text('Remark')
    abk_telephone = fields.Char('Telephone')
    abk_jobno = fields.Char('Job Number')
    abk_amendment = fields.Char('Amendement')
    abk_amenduser = fields.Char('Amendement User')
    abk_amenddate = fields.Datetime('Amendement Date')

    abk_produser = fields.Char('Production User')
    abk_stockqty = fields.Float('Stock quantity')
    abk_poqty = fields.Float('PO Quantity')
    abk_pounit = fields.Char('PO Unit')

    abk_delmark = fields.Text('Delivery Mark')
    abk_internalcode = fields.Char('Internal Code')
    abk_deladdress = fields.Text('Delivery Address')
    abk_receivequantity = fields.Float('Receive quantity')
    abk_not_yet_receive_quantity = fields.Char('Not yet receive quantity')
    abk_worksorder_number = fields.Char('Worksorder number')
    abk_tax = fields.Char('Tax')
    abk_potype = fields.Char('PO Type')
    abk_unitprice = fields.Monetary('Unit price')
    abk_extracost = fields.Monetary('Extra Cost')
    abk_materialduedate = fields.Datetime('Material Due Date')
    abk_sono = fields.Char('Sales order number')
    abk_sale_order_id = fields.Many2one('sale.order', string='Sale Order')


class PurchaseOrderLineCustom(models.Model):
    _inherit = 'purchase.order.line'

    abk_impt = fields.Char('Tax Type')
    abk_impt_1 = fields.Char('Tax Type')
    abk_size = fields.Char('Size')
    abk_actqty = fields.Float('Actual quantity')
    abk_fcolour = fields.Char('fcolour')
    abk_bcolour = fields.Char('bcolour')
    abk_chcolour = fields.Char('chcolour')
    abk_fcolourno = fields.Char('fcolourno')
    abk_bcolourno = fields.Char('bcolourno')
    abk_machine = fields.Char('Machine')
    abk_paper = fields.Char('Paper')
