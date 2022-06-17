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


class FinancialReportControllerInhe(http.Controller):

    @http.route('/prueba_addon/download_report_txt', type='http', auth='user')
    def report_txt(self, **kw):
        fp = tempfile.TemporaryFile('w+')
        invoices = request.env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', 'in', ['posted'])])
        report = ''
        for invoice in invoices:
            report += (invoice.invoice_date.strftime(
                    '%d/%m/%Y') if invoice else '') + '||'
            report += invoice.partner_id.name + ':' + invoice.partner_id.email + '||' + str(invoice.amount_tax) + '||' + str(invoice.amount_total)
            report += '|\n'
        fp.write(report)
        fp.seek(0)
        file_data = fp.read()
        fp.close()
        return request.make_response(
            file_data, headers=[
                ('Content-Disposition', 'attachment; filename="report_invoice.txt"'),
                ('Content-Type', 'text/plain')
            ]
        )
        
    @http.route('/prueba_addon/download_report_date_txt/<string:date_from>/<string:date_to>', type='http', auth='user')
    def report_date_txt(self, date_from, date_to, **kw):
        fp = tempfile.TemporaryFile('w+')
        invoices = request.env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', 'in', ['posted']), ('date', '>=', date_from), ('date', '<=', date_to)])
        report = ''
        for invoice in invoices:
            report += (invoice.invoice_date.strftime(
                    '%d/%m/%Y') if invoice else '') + '||'
            report += invoice.partner_id.name + ':' + invoice.partner_id.email + '||' + str(invoice.amount_tax) + '||' + str(invoice.amount_total)
            report += '|\n'
        fp.write(report)
        fp.seek(0)
        file_data = fp.read()
        fp.close()
        return request.make_response(
            file_data, headers=[
                ('Content-Disposition', 'attachment; filename="report_invoice.txt"'),
                ('Content-Type', 'text/plain')
            ]
        )
    


class ExcelExportView(ExcelExport):
    def __getattribute__(self, name):
        if name == 'fmt':
            raise AttributeError()
        return super(ExcelExportView, self).__getattribute__(name)

    @http.route('/prueba_addon/download_report_xls', type='http', auth='user')
    def download_xls_ple_sale(self, **kw):
        model = "report_xls"
        invoices = request.env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', 'in', ['posted'])])
        columns_headers = ['Cliente', 'Fecha de Factura', 'Numero', 'Moneda', 'Total']
        rows = []
        for invoice in invoices:
            rows.append([invoice.partner_id.name, invoice.invoice_date, invoice.name, invoice.company_currency_id.name, invoice.amount_total])

        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename="%s"'
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ]
        )


    @http.route('/prueba_addon/download_report_date_xls/<string:date_from>/<string:date_to>', type='http', auth='user')
    def download_xls_ple_sale(self, date_from, date_to, **kw):
        model = "report_xls"
        invoices = request.env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', 'in', ['posted']), ('date', '>=', date_from), ('date', '<=', date_to)])
        columns_headers = ['Cliente', 'Cliente Email', 'Fecha de Factura', 'Numero', 'Moneda', 'Total']
        rows = []
        for invoice in invoices:
            rows.append([invoice.partner_id.name, invoice.partner_id.email, invoice.invoice_date, invoice.name, invoice.company_currency_id.name, invoice.amount_total])

        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename="%s"'
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ]
        )
    