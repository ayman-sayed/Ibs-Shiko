# -*- coding: utf-8 -*-
# from odoo import http


# class AddButtonTransfer(http.Controller):
#     @http.route('/add_button_transfer/add_button_transfer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_button_transfer/add_button_transfer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_button_transfer.listing', {
#             'root': '/add_button_transfer/add_button_transfer',
#             'objects': http.request.env['add_button_transfer.add_button_transfer'].search([]),
#         })

#     @http.route('/add_button_transfer/add_button_transfer/objects/<model("add_button_transfer.add_button_transfer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_button_transfer.object', {
#             'object': obj
#         })
