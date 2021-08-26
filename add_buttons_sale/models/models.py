# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.product'

    @api.constrains('default_code')
    def make_code_unique(self):
        for rec in self:
            product=self.env['product.product'].search([('default_code','=',self.default_code),('id','!=',self.id)],limit=1)
            if product :
                raise UserError("This Product Code Exist Before")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('validate', 'Validate'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    type = fields.Selection(string="Type", selection=[('online', 'Online'), ('vip', 'VIP'), ], required=False,
                            compute="vip_or_online")

    def button_method_validate(self):
        for rec in self:
            rec.state = "validate"

    @api.depends('partner_id')
    def vip_or_online(self):
        for rec in self:
            res_user = self.env['res.users'].search([('id', '=', rec._uid)])
            if res_user.has_group('add_buttons_sale.id_group_vip'):
                rec.type = 'vip'
            elif res_user.has_group('add_buttons_sale.id_group_online'):
                rec.type = 'online'
            else:
                rec.type = 'online'

# class add_buttons_sale(models.Model):
#     _name = 'add_buttons_sale.add_buttons_sale'
#     _description = 'add_buttons_sale.add_buttons_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
