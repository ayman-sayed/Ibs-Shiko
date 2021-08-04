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
            order_linee = []
            for line in rec.packing_list:
                order_linee.append((0, 0, {
                    'product_id': line.product_id_id.id,
                    'name': line.product_description,
                    'product_qty': line.quantity,
                    'product_uom': line.product_id_id.uom_id.id,
                    'price_unit': 50,
                    'purchase_order_line':[ line.id]
                }))
            print('order_linee',order_linee)
            po_create=self.env['purchase.order'].sudo().create({
                    'partner_id': rec.vendor_name.id,
                    'order_line': order_linee,
                })
            rec.state = "create_po"
            return {
                'name': 'Purchase',
                'domain': [('id', '=', po_create.id)],
                'res_model': 'purchase.order',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                # 'view_type': 'form',
                'target': 'current',
            }



    # def tap_for_quotation(self):
    #     order_linee=[]
    #     attache=[]
    #     for rec in self:
    #         for attach in rec.attachment_ids:
    #             attache.append(attach.id)
    #         # rec.state="fully_quotationed"
    #         for line in rec.request_line_ids:
    #             if line.state != "fully_quotationed":
    #                 order_linee.append((0,0,{
    #             'product_id': line.product_id.id,
    #             'name': line.name,
    #             'product_qty': line.product_qty,
    #             'product_uom': line.product_uom_id.id,
    #             'attachmentt_ids': [a.id for a in line.attachment_ids],
    #             'purchase_requests_id': self.id,
    #             'purchase_request_line':[ line.id],
    #
    #         }))
    #                 print("order",order_linee)
    #
    #     return {
    #         'name': 'New Quotation',
    #         'domain': [],
    #         'res_model': 'purchase.order',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'view_type': 'form',
    #         'context': {
    #             "default_order_line" : order_linee,
    #             "default_date_planned" : self.due_date,
    #             "default_request_name" : self.nname,
    #             "default_purchase_requests" : self.id,
    #             "default_product_category_id" : self.request_category_id.id,
    #             "default_attachmentt_ids" : [i.id for i in self.attachment_ids],
    #             "default_purchase_request_ids" : [self.id],
    #
    #                     },
    #         'target': 'new',
    #     }

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

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
    product_description = fields.Char(string="Product Description",related='product_id_id.name', tracking=True)
    quantity = fields.Float(string="Quantity", tracking=True)
