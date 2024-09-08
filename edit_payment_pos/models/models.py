# -*- coding: utf-8 -*-

from odoo import models, fields, api



class StockQuant(models.Model):
    _inherit = 'stock.quant'

    container_no = fields.Char(string="Container No	", required=False,store=True)

