# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AddNewDisplay(models.Model):
    _name = 'add_new_display'
    _description = 'add_new_display'

    date = fields.Date(string="", required=False, )
    source_id = fields.Many2one(comodel_name="stock.location", string="", required=True)
    destination_id = fields.Many2one(comodel_name="stock.location", string="", required=True)
    Operation_type_id = fields.Many2one(comodel_name="stock.picking.type", string="", required=True)
    state = fields.Selection(string="", selection=[('draft', 'Draft'),
                                                   ('confirm', 'Confirm'),
                                                   ], required=False, default="draft")
    product_ids = fields.One2many(comodel_name="inventory_line", inverse_name="new_field_id", string="",
                                  required=False, )
    is_transfer = fields.Boolean(string="", default=False, copy=False)
    get_method = fields.Many2one(comodel_name="stock.picking", string="", required=False, )

    def confirm_display(self):
        for rec in self:
            rec.state = "confirm"

    def transfer_move(self):
        self.is_transfer = True
        product_line = []
        for rec in self:
            for line in rec.product_ids:
                product_line.append((0, 0, {'product_uom': line.new_product_id.uom_id.id,
                                            'name': line.new_product_id.name, 'product_uom_qty': line.qty,
                                            'product_id': line.new_product_id.id}))

            x = self.env['stock.picking'].create({
                'scheduled_date': rec.date,
                'location_id': rec.source_id.id,
                'location_dest_id': rec.destination_id.id,
                'picking_type_id': rec.Operation_type_id.id,
                'move_ids_without_package': product_line,
            })
            x.action_confirm()
