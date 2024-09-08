# -*- coding: utf-8 -*-
# from odoo import http


# class AddPackingListMenu(http.Controller):
#     @http.route('/add_packing_list_menu/add_packing_list_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_packing_list_menu/add_packing_list_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_packing_list_menu.listing', {
#             'root': '/add_packing_list_menu/add_packing_list_menu',
#             'objects': http.request.env['add_packing_list_menu.add_packing_list_menu'].search([]),
#         })

#     @http.route('/add_packing_list_menu/add_packing_list_menu/objects/<model("add_packing_list_menu.add_packing_list_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_packing_list_menu.object', {
#             'object': obj
#         })
