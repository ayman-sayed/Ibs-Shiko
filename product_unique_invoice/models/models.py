# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import ValidationError
import collections


class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_line_ids')
    def check_product_id(self):
        for rec in self:
            product = []
            for line in rec.invoice_line_ids:
                product.append(line.product_id.id)
            if ([item for item, count in collections.Counter(product).items() if count > 1]):
                raise ValidationError(_("يجب ان لا يتكرر المنتج"))
