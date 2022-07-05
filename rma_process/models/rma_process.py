from odoo import fields, models, api, _


class RmaProcess(models.Model):
    """rma process model"""

    _name = "rma.process"
    _description = "Rma Process"
    _rec_name = 'sale_order_id'

    customer_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Datetime(string='Date')
    rma_line_ids = fields.One2many('rma.order.line', 'rma_process_id', string='Lines')
    sale_order_id = fields.Many2one('sale.order')
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('completed', 'Completed')],
        help="state is used to separate Draft,Completed",
        default='draft')

    def button_validate(self):
        """button validate"""
        for invoice in self.sale_order_id.invoice_ids:

            action = self.env["ir.actions.actions"]._for_xml_id("account.action_view_account_move_reversal")

            if invoice.is_invoice():
                action['name'] = _('Credit Note')

            action['context'] = ({'rma_mov_ids': self.sale_order_id.invoice_ids.ids})
            self.state = 'completed'
            return action


class RmaOrderLine(models.Model):
    """ used to rma order line"""
    _name = 'rma.order.line'
    _description = "Rma Order Lines"
    product_id = fields.Many2one('product.product', string='Product')
    rma_process_id = fields.Many2one('rma.process', string='Rma Process')
    description = fields.Text(string='Description')
    quantity_product_uom = fields.Float(string='Quantity')
    delivered_qty = fields.Float(string='Delivery')
    invoiced_qty = fields.Float(string='Invoiced')
    unit_price = fields.Float(string='Unit Price')
    tax_id = fields.Many2many('account.tax', string='Taxes')
    sub_total = fields.Monetary()
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company.id)


class SaleOrder(models.Model):
    """used to sale order"""
    _inherit = 'sale.order'
    rma_process_id = fields.Many2one('rma.process')

    def rma_button(self):
        """rma button"""
        if not self.rma_process_id:
            rma = self.env['rma.process'].sudo().create({
                'customer_id': self.partner_id.id,
                'date': self.date_order,
                'sale_order_id': self.id

            })
            self.rma_process_id = rma.id
        else:
            rma = self.rma_process_id
        for line in self.order_line:
            if not line.rma_line_id:
                var = self.env['rma.order.line'].sudo().create({
                    'product_id': line.product_id.id,
                    'description': line.name,
                    'quantity_product_uom': line.product_uom_qty,
                    'delivered_qty': line.qty_delivered,
                    'invoiced_qty': line.qty_invoiced,
                    'unit_price': line.price_unit,
                    'tax_id': line.tax_id.ids,
                    'sub_total': line.price_subtotal,
                    'rma_process_id': rma.id

                })
                line.rma_line_id = var.id

    def get_rma(self):
        """get RMA process"""
        view = self.env.ref('rma_process.rma_process_views_form')
        return {
            'name': _('RMA'),
            'res_model': 'rma.process',
            'views': [(view.id, 'form'), ],
            'res_id': self.rma_process_id.id,
            'type': 'ir.actions.act_window',

            'target': 'current',
        }


class SaleOrderLine(models.Model):
    """sale order line"""
    _inherit = 'sale.order.line'

    rma_line_id = fields.Many2one('sale.order.line')


class AccountMoveReversal(models.TransientModel):
    """account move reversal"""
    _inherit = 'account.move.reversal'

    @api.model
    def default_get(self, fields):
        """default get"""
        res = super(AccountMoveReversal, self).default_get(fields)
        if self.env.context.get('active_model') == 'rma.process':
            move_ids = self.env['account.move'].browse(self.env.context['rma_mov_ids'])
            if 'move_ids' in fields:
                res['move_ids'] = [(6, 0, move_ids.ids)]
        res
        return res
