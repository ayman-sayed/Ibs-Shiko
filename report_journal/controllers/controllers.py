# -*- coding: utf-8 -*-
# from odoo import http


# class ReportJournal(http.Controller):
#     @http.route('/report_journal/report_journal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_journal/report_journal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_journal.listing', {
#             'root': '/report_journal/report_journal',
#             'objects': http.request.env['report_journal.report_journal'].search([]),
#         })

#     @http.route('/report_journal/report_journal/objects/<model("report_journal.report_journal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_journal.object', {
#             'object': obj
#         })
