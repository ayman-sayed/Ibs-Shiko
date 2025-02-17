# -*- coding: utf-8 -*-
from odoo import models, fields, api
class AccountMove(models.Model):
    _inherit = 'account.move'

    ibs_analytic_account = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        readonly=True,
    )

    @api.model
    def create(self, vals):
        if 'journal_id' in vals:
            journal = self.env['account.journal'].browse(vals['journal_id'])
            vals['ibs_analytic_account'] = journal.ibs_analytic_account.id if journal.ibs_analytic_account else False
        return super(AccountMove, self).create(vals)

    def write(self, vals):

        if 'journal_id' in vals:
            journal = self.env['account.journal'].browse(vals['journal_id'])
            vals['ibs_analytic_account'] = journal.ibs_analytic_account.id if journal.ibs_analytic_account else False
        return super(AccountMove, self).write(vals)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    ibs_analytic_account_line = fields.Many2one(
        'account.analytic.account',
        string=' Analytic Account ',
        compute='_compute_ibs_analytic_account_line',
        readonly=True,
    )


    @api.depends('account_id', 'move_id.ibs_analytic_account')
    def _compute_ibs_analytic_account_line(self):
        for line in self:
            # Accessing the account type
            account_type = line.account_id.account_type

            # If the account type is 'income', set the ibs_analytic_account_line
            if account_type == 'income':
                line.ibs_analytic_account_line = line.move_id.ibs_analytic_account
            else:
                line.ibs_analytic_account_line = False

            # Update the ibs_analytic_account in the AccountMove line
            if account_type == 'income':
                line.move_id.ibs_analytic_account = line.ibs_analytic_account_line