# -*- coding: utf-8 -*-
# from odoo import http


# class AddFieldSelcSale(http.Controller):
#     @http.route('/add_field_selc_sale/add_field_selc_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_field_selc_sale/add_field_selc_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_field_selc_sale.listing', {
#             'root': '/add_field_selc_sale/add_field_selc_sale',
#             'objects': http.request.env['add_field_selc_sale.add_field_selc_sale'].search([]),
#         })

#     @http.route('/add_field_selc_sale/add_field_selc_sale/objects/<model("add_field_selc_sale.add_field_selc_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_field_selc_sale.object', {
#             'object': obj
#         })
