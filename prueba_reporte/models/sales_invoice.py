from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class SalesInvoice(models.Model):
    _name= "sales.invoice"
    _description = "Factura de Ventas"
    