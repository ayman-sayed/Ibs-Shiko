# -*- coding: utf-8 -*-
# from odoo import http


# class AddButtons(http.Controller):
#     @http.route('/add_buttons/add_buttons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_buttons/add_buttons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_buttons.listing', {
#             'root': '/add_buttons/add_buttons',
#             'objects': http.request.env['add_buttons.add_buttons'].search([]),
#         })

#     @http.route('/add_buttons/add_buttons/objects/<model("add_buttons.add_buttons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_buttons.object', {
#             'object': obj
#         })
