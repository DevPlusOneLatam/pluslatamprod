import json

from odoo import http
from odoo import _, api, fields, models
from odoo.http import content_disposition, request
from odoo.addons.web.controllers.main import ExcelExport
from odoo.addons.web.controllers.main import _serialize_exception
from odoo.tools import html_escape
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
import json
import tempfile
import re
from datetime import datetime


class InvoiceReportView(ExcelExport):
    def __getattribute__(self,name):
        if name == 'fmt':
            raise AttributeError()
        return super(InvoiceReportView,self).__getattribute__(name)

    @http.route('/prueba_reporte/download_report_xls',type='http',auth='user')
    def download_xls_ple_sale(self, **kw):
        model = "report_xls"
        invoices = request.env['account.move'].search([('move_type','=','out_invoice')])
         # n_Factura,fecha_reg,fecha_venc,moneda,tipoCambio,cond_pago,nombre_cliente,ruc_cliente,total_sinIgv,igv,total_igv
        columns_headers = ['Nº Factura','Fecha Registro','Fecha Vencimiento','Moneda','Tipo Cambio','Condicion Pago','Nombre Cliente','Nº Ruc Cliente','Total Sin IGV','IGV','TOTAL CON IGV']
        rows = []
        for invoice in invoices:
            rows.append([invoice.name,invoice.invoice_date,invoice.invoice_date_due,invoice.currency_id,invoice.currency_id,invoice.payment_state,invoice.invoice_partner_display_name,invoice.partner_id.vat,invoice.amount_untaxed_signed,invoice.amount_tax_signed,invoice.amount_residual])

        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename='%s''
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ]
        )
