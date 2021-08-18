# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    transfer_count = fields.Integer(string='Transfer count', default=0, store=True, compute='_compute_transfer_count')
    is_transfer = fields.Boolean(string="", default=False, copy=False)
    date_transfer = fields.Date(string="Date Transfer", )

    @api.constrains('move_ids_without_package')
    def _compute_transfer_count(self):
        for rec in self:
            rec.transfer_count = len(rec.move_ids_without_package) / 2

    def internal_transfer(self):
        for rec in self:
            lines = []
            for line in rec.move_ids_without_package:
                lines.append([0, 0, {
                    'name': line.name,
                    'product_uom': line.product_uom,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.product_uom_qty,
                    'reserved_availability': line.reserved_availability,
                    'quantity_done': line.quantity_done,
                }])
            transfer = self.env['stock.picking'].sudo().create({
                'partner_id': rec.partner_id.id,
                'picking_type_id': self.env.ref('stock.picking_type_internal').id,
                'location_id': self.env.ref('stock.stock_location_stock').id,
                'location_dest_id': 18,
                'scheduled_date': rec.scheduled_date,
                'origin': rec.origin,
                'date_transfer': rec.date_transfer,
                'move_ids_without_package': lines,
            })
            rec.is_transfer = True
            # return {
            #     'view_mode': 'form',
            #     'res_model': 'stock.picking',
            #     'res_id': transfer.id,
            #     'type': 'ir.actions.act_window',
            #     'target': 'current'
            # }

    def button_internal_transfer(self):
        transfer = []
        for rec in self:
            for line in rec.move_ids_without_package:
                if line.product_id:
                    transfer.append(line.product_id.id)
        return {
            'name': _('Transfer'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('partner_id', '=', self.partner_id.id), ('date_transfer', '=', self.date_transfer),
                       ('scheduled_date', '=', self.scheduled_date),
                       ('id', '!=', self.id)],
        }
