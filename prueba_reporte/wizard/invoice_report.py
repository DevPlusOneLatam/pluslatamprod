from datetime import datetime, timedelta
from io import StringIO
import logging

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class InvoiceReport(models.TransientModel):
    _name= "invoice.report"
    _description = "Reporte Factura"

   # n_Factura,fecha_reg,fecha_venc,moneda,tipoCambio,cond_pago,nombre_cliente,ruc_cliente,total_sinIgv,igv,total_igv
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)

    def action_report(self):
        #custom_value={}

        #def convert_date(date):
           
        return {
            'name': 'FEC',
            'type': 'ir.actions.act_url',
            'url': '/prueba_reporte/download_report_xls/',
            'target': 'self',
        } 