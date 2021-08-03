# -*- coding: utf-8 -*-

from odoo import models, fields, api


class add_packing_list_menu(models.Model):
    _name = 'add_packing_list_menu.add_packing_list_menu'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'add_packing_list_menu_add_packing_list_menu'

    vendor_name = fields.Many2one(comodel_name="res.partner", string="Vendor Name ", tracking=True)
    vendor_address = fields.Char(string="Vendor Address & Tel", tracking=True)
    shipping_number = fields.Char(string="Shipping Number", tracking=True)
    container_number = fields.Char(string="Container Number", tracking=True)
    order_date = fields.Datetime(string="Ordered Date", tracking=True)
    delivery_date = fields.Datetime(string="Delivery Date", tracking=True)
    packing_list = fields.One2many(comodel_name="line.line", inverse_name="picking_id", string="Packing List",
                                   required=False, tracking=True)
    state = fields.Selection(string="State", selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                                                        ('create_po', 'Create_Po'), ], default="draft", tracking=True)

    def git_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def git_create_po(self):
        for rec in self:
            rec.state = "create_po"


class LineTap(models.Model):
    _name = 'line.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'line_line'

    product_id_id = fields.Many2one(comodel_name="product.product", string="Product", )
    picking_id = fields.Many2one(comodel_name="add_packing_list_menu.add_packing_list_menu", tracking=True)
    product_description = fields.Text(string="Product_Description", tracking=True)
    quantity = fields.Float(string="Quantity", tracking=True)
