from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class LetraInvoice(models.Model):
    _name = "letra.invoice"
    _description = "Letras de facturas"
    
    name = fields.Char(size=100, string='Nombre')
    type_letra = fields.Selection([('descuento', 'Letra en descuento'), ('cartera', 'Letra en Cartera')])
    invoice_id = fields.Many2one(comodel_name='account.move', string='Factura')
    amount_total = fields.Float(required=False, string='Valor de la letra')
    created_by = fields.Many2one(comodel_name='res.users', string='Vendedor', default=lambda self: self.env.user.id, index=1)
    letra_items_ids = fields.One2many('letra.invoice.item', 'letra_invoice_id', string='Item', readonly=False, copy=True)


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('letra.invoice')
        amount_total = 0.0
        for item_line in vals['letra_items_ids']:
            _logger.info(item_line)
            _logger.info(item_line[0])
            _logger.info(item_line[1])
            _logger.info(item_line[2])
            amount_total += item_line[2]['amount']
        vals['amount_total'] = amount_total
        res = super(LetraInvoice, self).create(vals)
        return res

    @api.model
    def write(self, vals):
        amount_total = 0.0
        for item_line in vals['letra_items_ids']:
            amount_total += item_line[2]['amount']
        vals['amount_total'] = amount_total
        res = super(LetraInvoice, self).create(vals)
        return res