# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class EditAccountMove(models.Model):
    _inherit = 'account.move'

    collection_ids = fields.One2many(comodel_name="collection", inverse_name="move_id", string="Collections", required=False, )

#
# class AccountJournal(models.Model):
#     _inherit = 'account.journal'
#
#     next_link_synchronization = fields.Float(string="", required=False, )
#     account_online_account_id = fields.Many2one(comodel_name="account.account", string="", required=False, )
#     account_online_link_state = fields.Float(string="", required=False, )
#     bank_statement_creation_groupby = fields.Float(string="", required=False, )

    def button_draft(self):
        AccountMoveLine = self.env['account.move.line']
        excluded_move_ids = []

        if self._context.get('suspense_moves_mode'):
            excluded_move_ids = AccountMoveLine.search(AccountMoveLine._get_suspense_moves_domain() + [('move_id', 'in', self.ids)]).mapped('move_id').ids

        for move in self:
            if move in move.line_ids.mapped('full_reconcile_id.exchange_move_id'):
                raise UserError(_('You cannot reset to draft an exchange difference journal entry.'))
            if move.tax_cash_basis_rec_id:
                raise UserError(_('You cannot reset to draft a tax cash basis journal entry.'))
            # قم بإلغاء الشرط التالي
            # if move.restrict_mode_hash_table and move.state == 'posted' and move.id not in excluded_move_ids:
            #    raise UserError(_('You cannot modify a posted entry of this journal because it is in strict mode.'))
            # نحن نحذف جميع الإدخالات التحليلية لهذا الجورنال
            move.mapped('line_ids.analytic_line_ids').unlink()

        self.mapped('line_ids').remove_move_reconcile()
        self.write({'state': 'draft'})

    # def server_button_draft(self):
    #     for rec in self:
    #         rec.write({'state': 'draft'})

class Collection(models.Model):
    _name = 'collection'
    _description = 'Collection'

    date = fields.Date(string="Date", required=True, )
    amount = fields.Float(string="Amount",  required=True, )
    move_id = fields.Many2one(comodel_name="account.move", string="Inv", required=False, )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=False,related='move_id.partner_id' )

