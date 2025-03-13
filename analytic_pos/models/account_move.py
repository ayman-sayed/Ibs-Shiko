# -*- coding: utf-8 -*-
from odoo import models, fields, api
class AccountMove(models.Model):
    _inherit = 'account.move'

    ibs_analytic_account = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',

        readonly=True,
    )
    ibs_analytic_distribution = fields.Json(
        string='Analytic Distribution',
    )
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get("Percentage Analytic"),
    )



    @api.model
    def create(self, vals):
        analytic_distribution = {}
        if 'journal_id' in vals:
            journal = self.env['account.journal'].browse(vals['journal_id'])
            vals['ibs_analytic_account'] = journal.ibs_analytic_account.id if journal.ibs_analytic_account else False

            if journal.ibs_analytic_account:
                analytic_distribution[journal.ibs_analytic_account.id] = 100
                vals['ibs_analytic_distribution'] = analytic_distribution
                for line in self.invoice_line_ids:
                    line.analytic_distribution = analytic_distribution

        return super(AccountMove, self).create(vals)

    def write(self, vals):
        analytic_distribution = {}
        if 'journal_id' in vals:
            journal = self.env['account.journal'].browse(vals['journal_id'])
            vals['ibs_analytic_account'] = journal.ibs_analytic_account.id if journal.ibs_analytic_account else False

            if journal.ibs_analytic_account:
                analytic_distribution[journal.ibs_analytic_account.id] = 100
                vals['ibs_analytic_distribution'] = analytic_distribution
                for line in self.invoice_line_ids:
                    line.analytic_distribution = analytic_distribution
        return super(AccountMove, self).write(vals)






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    ibs_analytic_account_line = fields.Many2one(
        'account.analytic.account',
        string=' Analytic Account ',
        compute='_compute_ibs_analytic_account_line',

        readonly=True,
    )

    analytic_distribution = fields.Json(
        inverse="_inverse_analytic_distribution",
        string='Analytic Distribution',
        readonly=False,
        compute='_ibs_compute_analytic_distribution',
        store=True,
    )

    @api.depends('move_id.ibs_analytic_distribution')
    def _ibs_compute_analytic_distribution(self):
        for line in self:
            if line.move_id.ibs_analytic_distribution:
                line.analytic_distribution = line.move_id.ibs_analytic_distribution
            else:
                line.analytic_distribution = {}

    # @api.model
    # def create(self, vals):
    #     if 'move_id' in vals:
    #         move = self.env['account.move'].browse(vals['move_id'])
    #         if move.ibs_analytic_distribution:
    #             vals['analytic_distribution'] = move.ibs_analytic_distribution
    #     return super(AccountMoveLine, self).create(vals)
    #
    # def write(self, vals):
    #     if 'move_id' in vals:
    #         move = self.env['account.move'].browse(vals['move_id'])
    #         if move.ibs_analytic_distribution:
    #             vals['analytic_distribution'] = move.ibs_analytic_distribution
    #     return super(AccountMoveLine, self).write(vals)





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





    # @api.onchange('ibs_analytic_account_line')
    # def distribution_onchange(self):
    #     analytic_distribution = {}
    #     for line in self:
    #         # Ensure that the ibs_analytic_account exists and directly access its attributes
    #         if line.move_id.ibs_analytic_account:
    #             analytic_account_id = line.move_id.ibs_analytic_account.id
    #             analytic_account_name = line.move_id.ibs_analytic_account.name if line.move_id.ibs_analytic_account else 'No Account'
    #         else:
    #             analytic_account_id = False
    #             analytic_account_name = 'No Account'
    #
    #         analytic_distribution[analytic_account_id] = 100
    #         line.analytic_distribution = analytic_distribution
    #         print('line.analytic_distribution', line.analytic_distribution)





