from datetime import datetime, timedelta
from io import StringIO
import logging

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class FacturaVentaReport(models.TransientModel):
    _name= "invoice.report"
    _description = "Reporte Factura"

   # n_Factura,fecha_reg,fecha_venc,moneda,tipoCambio,cond_pago,nombre_cliente,ruc_cliente,total_sinIgv,igv,total_igv

    def action_report(self):
        custom_value={}

        def convert_date(date):
            #dt = datetime.strptime(date, "%Y-%m-%d")
        return {
            'name': 'FEC',
            'type': 'ir.actions.act_url',
            'url': '/prueba_reporte/download_report_xls/',
            'target': 'self',
        } 