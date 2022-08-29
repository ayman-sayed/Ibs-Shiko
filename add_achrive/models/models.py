# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(
        default=True, )





class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    active = fields.Boolean(
        default=True, )


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    active = fields.Boolean(
        default=True, )


class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    active = fields.Boolean(
        default=True, )


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    active = fields.Boolean(
        default=True, )
