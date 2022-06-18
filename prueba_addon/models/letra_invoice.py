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
    invoice_draft_id = fields.Many2one(comodel_name='account.move', string='Factura borrador', domain="[('state', 'in', ['draft']), ('move_type', '=', 'out_invoice')]")
    amount_total = fields.Float(required=False, string='Valor de la letra')
    created_by = fields.Many2one(comodel_name='res.users', string='Vendedor', default=lambda self: self.env.user.id, index=1)



    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('letra.invoice')
        res = super(LetraInvoice, self).create(vals)
        return res
