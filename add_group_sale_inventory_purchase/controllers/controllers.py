# -*- coding: utf-8 -*-
# from odoo import http


# class AddGroupSaleInventoryPurchase(http.Controller):
#     @http.route('/add_group_sale_inventory_purchase/add_group_sale_inventory_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_group_sale_inventory_purchase/add_group_sale_inventory_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_group_sale_inventory_purchase.listing', {
#             'root': '/add_group_sale_inventory_purchase/add_group_sale_inventory_purchase',
#             'objects': http.request.env['add_group_sale_inventory_purchase.add_group_sale_inventory_purchase'].search([]),
#         })

#     @http.route('/add_group_sale_inventory_purchase/add_group_sale_inventory_purchase/objects/<model("add_group_sale_inventory_purchase.add_group_sale_inventory_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_group_sale_inventory_purchase.object', {
#             'object': obj
#         })
