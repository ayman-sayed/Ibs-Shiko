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
            print('rec.vendor_name.id', rec.vendor_name.id)
            print('rec.vendor_name.name', rec.vendor_name.name)
            po_create = self.env['purchase.order'].sudo().create({
                'partner_id': rec.vendor_name.id,
            })

            for line in rec.packing_list:
                order_linee = self.env['purchase.order.line'].sudo().create({
                    'product_id': line.product_id_id.id,
                    'name': line.product_description,
                    'product_qty': line.quantity,
                    'product_uom': line.product_id_id.uom_id.id,
                    'price_unit': 0,
                    'order_id': po_create.id
                })
            rec.state = "create_po"
            return {
                'name': 'Purchase',
                'res_id': po_create.id,
                'res_model': 'purchase.order',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                # 'view_type': 'form',
                'target': 'current',
            }




class PurchaseOrder(models.Model):
    _inherit = 'purchase.order.line'

    _sql_constraints = [
        ('accountable_required_fields',
         "CHECK(1=1)",
         "Missing required fields on accountable purchase order line."),
        ('non_accountable_null_fields',
         "CHECK(1=1)",
         "Forbidden values on non-accountable purchase order line"),
    ]


class LineTap(models.Model):
    _name = 'line.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'line_line'

    product_id_id = fields.Many2one(comodel_name="product.product", string="Product", )
    picking_id = fields.Many2one(comodel_name="add_packing_list_menu.add_packing_list_menu", tracking=True)
    product_description = fields.Char(string="Product Description", related='product_id_id.name', tracking=True)
    quantity = fields.Float(string="Quantity", tracking=True)
