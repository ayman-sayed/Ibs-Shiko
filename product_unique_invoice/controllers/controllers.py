# -*- coding: utf-8 -*-
# from odoo import http


# class ProductUniqueInvoice(http.Controller):
#     @http.route('/product_unique_invoice/product_unique_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_unique_invoice/product_unique_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_unique_invoice.listing', {
#             'root': '/product_unique_invoice/product_unique_invoice',
#             'objects': http.request.env['product_unique_invoice.product_unique_invoice'].search([]),
#         })

#     @http.route('/product_unique_invoice/product_unique_invoice/objects/<model("product_unique_invoice.product_unique_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_unique_invoice.object', {
#             'object': obj
#         })
