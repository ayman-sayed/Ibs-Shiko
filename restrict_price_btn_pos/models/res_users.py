# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    """Inherit res users and added new fields"""
    _inherit = 'res.users'
    price = fields.Boolean(string="Restrict POS Price", help="To hide price in pos "
                                                "session")

class PosOrder(models.Model):
    _inherit='pos.order'
