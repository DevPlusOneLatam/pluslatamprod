from datetime import datetime, timedelta
from io import StringIO
import logging

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class LetraReport(models.TransientModel):
    _name = "letra.report"
    _description = "Reporte de Letras"
    
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    date_from = fields.Date('Desde', required=True)
    date_to = fields.Date('Hasta', required=True)
    
    def action_report_txt(self): 
        custom_value = {}   
        
        def convert_date(date):
            dt = datetime.strptime(date, "%Y-%m-%d")
            return dt.strftime("%d%m%Y")
        
        _logger.info('Fecha de inicio: ' + str(self.date_from))
        _logger.error('Fecha final: ' + str(self.date_to))
        return {
            'name': 'FEC',
            'type': 'ir.actions.act_url',
            'url': '/prueba_addon/download_report_date_txt/' + str(self.date_from) + '/' + str(self.date_to),
            'target': 'self',
        }
    
    def action_report_xls(self):
        return {
            'name': 'FEC',
            'type': 'ir.actions.act_url',
            'url': '/prueba_addon/download_report_date_xls/' + str(self.date_from) + '/' + str(self.date_to),
            'target': 'self',
        }
