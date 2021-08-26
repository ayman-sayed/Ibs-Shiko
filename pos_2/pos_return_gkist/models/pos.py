# Copyright 2018-2019 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class pos_order(models.Model) :
    _inherit = 'pos.order'

    pos_config_id = fields.Many2one(comodel_name="pos.config", string="Point of Sale", required=False, )

    def refund(self):
        """Create a copy of order  for refund order"""
        refund_orders = self.env['pos.order']
        for order in self:
            # When a refund is performed, we are creating it in a session having the same config as the original
            # order. It can be the same session, or if it has been closed the new one that has been opened.
            current_session = order.session_id.config_id.current_session_id
            if not current_session:
                raise UserError(_('To return product(s), you need to open a session in the POS %s',
                                  order.session_id.config_id.display_name))
            orders = self.env['pos.order'].search([('name', '=', self.name + _(' REFUND')),
                                                  ('session_id', '=', self.session_id.id)])
            refund_order = order.copy(
                order._prepare_refund_values(current_session)
            )
            lines = self.env['pos.order.line'].search([('order_id','in',orders.ids)])

            for line in order.lines:
                PosOrderLineLot = self.env['pos.pack.operation.lot']
                for pack_lot in line.pack_lot_ids:
                    PosOrderLineLot += pack_lot.copy()
                line.copy(line._prepare_refund_data(refund_order, PosOrderLineLot))
            refund_orders |= refund_order

            for line in lines:
                refund_order_line = self.env['pos.order.line'].search([('order_id', '=', refund_orders.ids[0]),('product_id','=',line.product_id.id)])
                if refund_order_line:
                    refund_order_line.qty -= line.qty
                    # refund_order_line.field_name=refund_order_line.qty

                if refund_order_line.qty >= 0:
                    refund_order_line.sudo().unlink()
                    order = self.env['pos.order'].search([('id', '=', refund_orders.ids[0])])
                    order.sudo()._onchange_amount_all()

            pos_order= self.env['pos.order'].search([('id', '=', refund_orders.ids[0])])
            if not pos_order.lines:
                raise ValidationError(_("you can't return it"))


            employee = self.env['hr.employee'].sudo().search([('user_id','=',self.env.user.id)],limit=1)
            pos_order.pos_config_id = self.env['pos.config'].sudo().search([('employee_ids','in',employee.id)]).id
            pos_order.session_id = self.env['pos.session'].sudo().search([('config_id','=',pos_order.pos_config_id.id),('state','=','opened')]).id


        return {
            'name': _('Return Products'),
            'view_mode': 'form',
            'res_model': 'pos.order',
            'res_id': refund_orders.ids[0],
            'view_id': False,
            'context': self.env.context,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def _prepare_refund_values(self, current_session):
        self.ensure_one()
        return {
            'name': self.name + _(' REFUND'),
            'session_id': current_session.id,
            'date_order': fields.Datetime.now(),
            'pos_reference': self.pos_reference + (' (R)'),
            'lines': False,
            'amount_tax': -self.amount_tax,
            'amount_total': -self.amount_total,
            'amount_paid': 0,
        }