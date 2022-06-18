from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class LetraInvoice(models.Model):
    _name = "letra.invoice.item"
    _description = "Detalle de Letras de facturas"
    
    letra_invoice_id = fields.Many2one(comodel_name='letra.invoice', string='Letra')
    label = fields.Char(size=100, string='Label')
    amount = fields.Float(required=False, string='Valor del item')
