from odoo import models, fields

class POSReturnReasonWizard(models.TransientModel):
    _name = 'pos.return.reason.wizard'
    _description = 'POS Return Reason Wizard'

    return_reason = fields.Text(string="Return Reason", required=True)

    def confirm_return(self):
        order_id = self.env.context.get('active_id')
        order = self.env['pos.order'].browse(order_id)
        if order:
            order.write({'return_reason': self.return_reason})
            order.write({'state': 'draft'})
