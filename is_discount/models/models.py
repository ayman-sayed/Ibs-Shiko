# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IsDiscount(models.Model):
    _inherit = 'product.product'

    is_discount = fields.Boolean(string="Is Discount", )

