# -*- coding: utf-8 -*-

from odoo import models, fields,api,_
from odoo.exceptions import UserError

class PosSession(models.Model):
    _inherit = 'pos.session'

    account_analytic_id = fields.Many2one('account.analytic.account',
        related="config_id.account_analytic_id",
        store=True, string='Analytic Account', copy=False
    )

    # @api.model
    # def create(self, values):
    #     config_id = values.get('config_id') or self.env.context.get('default_config_id')
    #     if not config_id:
    #         raise UserError(_("You should assign a Point of Sale to your session."))

    #     # journal_id is not required on the pos_config because it does not
    #     # exists at the installation. If nothing is configured at the
    #     # installation we do the minimal configuration. Impossible to do in
    #     # the .xml files as the CoA is not yet installed.
    #     pos_config = self.env['pos.config'].browse(config_id)
    #     ctx = dict(self.env.context, company_id=pos_config.company_id.id)

    #     pos_name = self.env['ir.sequence'].with_context(ctx).next_by_code('pos.session')
    #     if values.get('name'):
    #         pos_name += ' ' + values['name']

    #     cash_payment_methods = pos_config.payment_method_ids.filtered(lambda pm: pm.is_cash_count)
    #     statement_ids = self.env['account.bank.statement']
    #     if self.user_has_groups('point_of_sale.group_pos_user'):
    #         statement_ids = statement_ids.sudo()
    #     for cash_journal in cash_payment_methods.mapped('journal_id'):
    #         ctx['journal_id'] = cash_journal.id if pos_config.cash_control and cash_journal.type == 'cash' else False
    #         st_values = {
    #             'journal_id': cash_journal.id,
    #             'user_id': self.env.user.id,
    #             'name': pos_name, 
    #             'account_analytic_id':self.account_analytic_id.id or False
    #         }
    #         print(self.account_analytic_id,"================")
    #         statement_ids |= statement_ids.with_context(ctx).create(st_values)

    #     update_stock_at_closing = pos_config.company_id.point_of_sale_update_stock_quantities == "closing"

    #     values.update({
    #         'statement_ids': [(6, 0, statement_ids.ids)],
    #         'config_id': config_id,
    #         'update_stock_at_closing': update_stock_at_closing,
    #     })

    #     if self.user_has_groups('point_of_sale.group_pos_user'):
    #         res = super(PosSession, self.with_context(ctx).sudo()).create(values)
    #     else:
    #         res = super(PosSession, self.with_context(ctx)).create(values)
    #     res.action_pos_session_open()

    #     return res

    def _get_stock_expense_vals(self, exp_account, amount, amount_converted):
        res = super(PosSession, self)._get_stock_expense_vals(exp_account, amount, amount_converted)
        if self.company_id.anglo_saxon_accounting:
            res['analytic_account_id'] = self.account_analytic_id.id or False
        return res

    def _get_stock_output_vals(self, out_account, amount, amount_converted):
        res = super(PosSession, self)._get_stock_output_vals(out_account, amount, amount_converted)
        if not self.company_id.anglo_saxon_accounting:
            res['analytic_account_id'] = self.account_analytic_id.id or False
        return res

    def _prepare_line(self, order_line):
        res = super(PosSession, self)._prepare_line(order_line)
        res['analytic_account_id'] = order_line.order_id.account_analytic_id or False
        return res

    def _get_sale_vals(self, key, amount, amount_converted,):
        res = super(PosSession, self)._get_sale_vals(key, amount, amount_converted)
        res['analytic_account_id'] = self.account_analytic_id.id or False
        return res

    def _get_invoice_receivable_vals(self, amount, amount_converted):
        res = super(PosSession, self)._get_invoice_receivable_vals(amount, amount_converted)
        res['analytic_account_id'] = self.account_analytic_id.id or False
        return res
