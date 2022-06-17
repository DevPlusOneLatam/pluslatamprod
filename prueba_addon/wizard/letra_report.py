# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import shutil, os
import time
from datetime import datetime, timedelta
import unicodedata
import base64
import io
from io import StringIO

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

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
        
        return {
            'name': 'FEC',
            'type': 'ir.actions.act_url',
            'url': '/prueba_addon/download_report_date_txt/' + str(self.date_from) + '/' + str(self.date_to),
            'target': 'self',
        }
    