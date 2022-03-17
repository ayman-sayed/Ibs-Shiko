# -*- coding: utf-8 -*-
# from odoo import http


# class EditPaymentPos(http.Controller):
#     @http.route('/edit_payment_pos/edit_payment_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_payment_pos/edit_payment_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_payment_pos.listing', {
#             'root': '/edit_payment_pos/edit_payment_pos',
#             'objects': http.request.env['edit_payment_pos.edit_payment_pos'].search([]),
#         })

#     @http.route('/edit_payment_pos/edit_payment_pos/objects/<model("edit_payment_pos.edit_payment_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_payment_pos.object', {
#             'object': obj
#         })
