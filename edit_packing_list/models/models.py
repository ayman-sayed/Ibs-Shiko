# -*- coding: utf-8 -*-

from odoo import models


class add_packing_list_menuadd_packing_list_menu(models.Model):
    _inherit = 'add_packing_list_menu.add_packing_list_menu'

    def git_create_po(self):
	global po_create
        po_create = super(add_packing_list_menuadd_packing_list_menu, self).git_create_po()
        for rec in self:
            po_create['date_planned'] = rec.delivery_date
        return po_create
