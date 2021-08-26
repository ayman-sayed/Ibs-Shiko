# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BroductDiscount(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('product_id', 'price_unit')
    def get_discount(self):
        for rec in self:
            if rec.product_id.is_discount and rec.price_unit > 0:
                rec.price_unit = -rec.price_unit




