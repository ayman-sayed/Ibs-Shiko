# -*- coding: utf-8 -*-
# from odoo import http


# class EditCollectionAccount(http.Controller):
#     @http.route('/edit_collection_account/edit_collection_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_collection_account/edit_collection_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_collection_account.listing', {
#             'root': '/edit_collection_account/edit_collection_account',
#             'objects': http.request.env['edit_collection_account.edit_collection_account'].search([]),
#         })

#     @http.route('/edit_collection_account/edit_collection_account/objects/<model("edit_collection_account.edit_collection_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_collection_account.object', {
#             'object': obj
#         })
