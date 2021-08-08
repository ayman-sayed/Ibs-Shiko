# -*- coding: utf-8 -*-
# from odoo import http


# class EditPackingList(http.Controller):
#     @http.route('/edit_packing_list/edit_packing_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_packing_list/edit_packing_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_packing_list.listing', {
#             'root': '/edit_packing_list/edit_packing_list',
#             'objects': http.request.env['edit_packing_list.edit_packing_list'].search([]),
#         })

#     @http.route('/edit_packing_list/edit_packing_list/objects/<model("edit_packing_list.edit_packing_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_packing_list.object', {
#             'object': obj
#         })
