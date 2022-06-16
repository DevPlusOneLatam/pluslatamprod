from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class LetraInvoice(models.Model):
    _name = "letra.invoice"
    _description = "Letras de facturas"
    
    type_letra = fields.Selection([('descuento', 'Letra en descuento'), ('cartera', 'Letra en Cartera')])
    invoice_id = fields.Many2one(comodel_name='account.move', string='Factura')
    amount_total = fields.Float(required=False, string='Valor de la letra')