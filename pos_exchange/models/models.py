# -*- coding: utf-8 -*-

from odoo import models, fields, api,_,exceptions
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError



class pos_exchange(models.Model):
    _inherit = 'pos.order'
    _description = 'POS exchange products'

    chek_box = fields.Boolean(string='box')

    header = fields.Char(string='header', compute="_get_header_and_footer")
    footer = fields.Char(string='footer', compute="_get_header_and_footer")

    def _get_header_and_footer(self):
        pos_header = self.env["pos.config"].search([('receipt_header', '!=', False)])
        self.header = pos_header.receipt_header
        self.footer = pos_header.receipt_footer


# class pos_exchan(models.Model):
#     _inherit = 'pos.order.line'
#     _description = 'POS exchange products'
#
#     chek_box = fields.Boolean(string='box')
#     themain_qty = fields.Float(string='main qty')
#
#
#
#     def _prepare_refund_data(self, refund_order, PosOrderLineLot):
#         """
#         This prepares data for refund order line. Inheritance may inject more data here
#
#         @param refund_order: the pre-created refund order
#         @type refund_order: pos.order
#
#         @param PosOrderLineLot: the pre-created Pack operation Lot
#         @type PosOrderLineLot: pos.pack.operation.lot
#
#         @return: dictionary of data which is for creating a refund order line from the original line
#         @rtype: dict
#         """
#         self.ensure_one()
#         return {
#             'name': self.name + _(' REFUND'),
#             'qty': -self.qty,
#             'chek_box': True,
#             'order_id': refund_order.id,
#             'price_subtotal': -self.price_subtotal,
#             'price_subtotal_incl': -self.price_subtotal_incl,
#             'pack_lot_ids': PosOrderLineLot,
#             'themain_qty': -self.qty,
#         }



    # @api.constrains('themain_qty', 'qty')
    # def gamal(self):
    #     for rec in self:
    #
    #         if rec.chek_box == True:
    #             if rec.qty > 0:
    #                 raise ValidationError(_("you cann't sell it again "))
    #
    #             if rec.qty < rec.themain_qty:
    #                 raise ValidationError(_("you cann't sell more than Quantity"))
    #
    #         else:
    #             if rec.qty < 0:
    #
    #                 raise ValidationError(_("you cann't return it"))
    #



