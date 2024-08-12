from odoo import models, fields

class POSOrder(models.Model):
    _inherit = 'pos.order'

    return_reason = fields.Text(string="Return Reason")

