# -*- coding: utf-8 -*-
# from odoo import http


# class IsDiscount(http.Controller):
#     @http.route('/is_discount/is_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/is_discount/is_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('is_discount.listing', {
#             'root': '/is_discount/is_discount',
#             'objects': http.request.env['is_discount.is_discount'].search([]),
#         })

#     @http.route('/is_discount/is_discount/objects/<model("is_discount.is_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('is_discount.object', {
#             'object': obj
#         })
