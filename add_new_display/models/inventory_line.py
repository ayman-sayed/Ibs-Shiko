# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InventoryLine(models.Model):
    _name = 'inventory_line'
    _description = 'inventory_line'

    new_field_id = fields.Many2one(comodel_name="add_new_display", string="", required=False, )
    new_product_id = fields.Many2one(comodel_name="product.product", string="Product", required=False, )
    qty = fields.Float(string="", required=False, )
