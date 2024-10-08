# -*- coding: utf-8 -*-
# from odoo import http


# class AddButtonsSale(http.Controller):
#     @http.route('/add_buttons_sale/add_buttons_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_buttons_sale/add_buttons_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_buttons_sale.listing', {
#             'root': '/add_buttons_sale/add_buttons_sale',
#             'objects': http.request.env['add_buttons_sale.add_buttons_sale'].search([]),
#         })

#     @http.route('/add_buttons_sale/add_buttons_sale/objects/<model("add_buttons_sale.add_buttons_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_buttons_sale.object', {
#             'object': obj
#         })
