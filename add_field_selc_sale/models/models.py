# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    Shipping_way = fields.Selection(string="Shipping Way",
                                    selection=[('customer_shipping', 'شحن للعميل '),
                                               ('bab_alshieria', 'إستلام من فرع باب الشعرية'),
                                               ('outlet_branch', 'إستلام من فرع Outlet'),
                                               ('book_branch', 'إستلام من فرع بوك'),
                                               ('bag_branch', 'إستلام من فرع شنطة'),
                                               ('main_stock', 'إستلام من المخزن الرئيسى'),
                                               ('sub_stock', 'إستلام من المخزن الفرعى'), ])

# class add_field_selc_sale(models.Model):
#     _name = 'add_field_selc_sale.add_field_selc_sale'
#     _description = 'add_field_selc_sale.add_field_selc_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
