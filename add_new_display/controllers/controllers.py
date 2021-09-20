# -*- coding: utf-8 -*-
# from odoo import http


# class AddNewDisplay(http.Controller):
#     @http.route('/add_new_display/add_new_display/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_new_display/add_new_display/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_new_display.listing', {
#             'root': '/add_new_display/add_new_display',
#             'objects': http.request.env['add_new_display.add_new_display'].search([]),
#         })

#     @http.route('/add_new_display/add_new_display/objects/<model("add_new_display.add_new_display"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_new_display.object', {
#             'object': obj
#         })
