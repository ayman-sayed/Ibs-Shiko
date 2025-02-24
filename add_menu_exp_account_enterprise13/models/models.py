# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_created = fields.Boolean(string="", defult=False)


class Expense(models.Model):
    _name = 'expense.expense'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'expense_expense'

    name = fields.Text(string="Ref", required=False, )
    journal_entry_id = fields.Many2one(comodel_name="account.move", string="Journal Entry", )
    expense_date = fields.Date(string="Expense Date", required=False, tracking=True)
    journal_id = fields.Many2one(comodel_name="account.journal", string="Journal", required=True, tracking=True,
                                 domain="[('type', 'in', ['bank','cash'])]")
    expenses_ids = fields.One2many(comodel_name="expense.line", inverse_name="invoice_id", string="Expenses",
                                   tracking=True)
    total = fields.Float(string="Total", tracking=True)
    tax = fields.Float(string="Taxes", compute="_get_tax", tracking=True)
    state = fields.Selection(selection=
                             [('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ], required=False, default='draft', tracking=True)
    amount_taxed = fields.Float(string="Un Taxed Amount", tracking=True)
    seq = fields.Char(readonly=True, copy=False, )

    def unlink(self):
        error_message = _('You cannot delete a expense which is in %s state')
        state_description_values = {elem[0]: elem[1] for elem in self._fields['state']._description_selection(self.env)}

        if self.user_has_groups('base.group_user'):
            if any(hol.state not in ['draft'] for hol in self):
                raise UserError(error_message % state_description_values.get(self[:1].state))
        return super(Expense, self).unlink()

    @api.model
    def create(self, vals):
        if vals.get('seq', _('New')) == _('New'):
            vals['seq'] = self.env['ir.sequence'].next_by_code(
                'expense.sequence', ) or _('New')
        result = super(Expense, self).create(vals)
        return result

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            rec.journal_entry_id.button_draft()

    def get_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def get_confirm(self):
        for rec in self:
            lines = []
            taxx = 0
            for line in rec.expenses_ids:
                for tax in line.tax_ids.invoice_repartition_line_ids:
                    if tax.account_id:
                        taxx = tax.account_id.id
                lines.append([0, 0, {
                    'account_id': line.account_id.id,
                    'analytic_account_id': line.analytic_account_id.id,
                    'name': line.name,
                    'debit': line.price_subtotal,
                    'expense_line_id': line.id,  # Set the expense line ID here
                    'analytic_distribution': line.analytic_distribution,  # Add this line

                }])
            if taxx:
                lines.append([0, 0, {
                    'account_id': taxx,
                    'name': 'tax',
                    'debit': rec.tax,
                }])
            lines.append([0, 0, {
                'account_id': rec.journal_id.default_account_id.id,
                'name': rec.name,
                'credit': rec.total,
            }])

            if rec.journal_entry_id.is_created == False:
                invoice = self.env['account.move'].sudo().create({
                    'is_created': True,
                    'move_type': 'entry',
                    'ref': rec.name,
                    'date': rec.expense_date,
                    'journal_id': rec.journal_id.id,
                    'line_ids': lines,
                })
                rec.journal_entry_id = invoice.id
                invoice.action_post()

                # 'line_ids': [(0, 0, {
                #         'account_id': rec.account_id.id,
                #         'name': rec.name,
                #         'debit': rec.price_unit,
                #     }), (0, 0, {
                #         'account_id': rec.account_id.id,
                #         'name': rec.name,
                #         'credit': rec.price_unit,
                #     })],
                # })
                # rec.journal_entry_id = invoice.id
            else:
                rec.journal_entry_id.date = rec.expense_date
                rec.journal_entry_id.journal_id = rec.journal_id
                rec.journal_entry_id.ref = rec.name
                rec.journal_entry_id.line_ids = False
                rec.journal_entry_id.line_ids = lines
                rec.journal_entry_id.action_post()
            rec.state = 'confirm'

    @api.depends("expenses_ids")
    def _get_tax(self):
        subtotal = 0
        for rec in self:
            n = 0
            taxes = 0
            for line in rec.expenses_ids:
                t = 0
                for any_line in line.tax_ids:
                    t = t + any_line.amount
                taxes = (t / 100) * line.quantity * line.price_unit
                line.price_subtotal = line.quantity * line.price_unit
                subtotal = subtotal + line.price_subtotal
                n = n + taxes
            rec.tax = n
            rec.amount_taxed = subtotal
            rec.total = rec.tax + rec.amount_taxed


class ExpenseLine(models.Model):
    _name = 'expense.line'
    _description = 'expense_line'

    invoice_id = fields.Many2one(comodel_name="expense.expense", )
    product_ids = fields.Many2one(comodel_name="product.product", string="Product", )
    name = fields.Char(string="Label", )
    account_id = fields.Many2one(comodel_name="account.account", string="Account", required=True, )
    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account ",
                                          required=False,store=True )
    quantity = fields.Float(string="Quantity", required=False, default="1")
    price_unit = fields.Float(string="Price", required=True, )
    tax_ids = fields.Many2many(comodel_name="account.tax", string="Taxes", )
    price_subtotal = fields.Float(string="Subtotal", required=False, )
    # tax_value = fields.Float(string="Taxes Value", )
    # subtotal = fields.Float(string="Subtotal Go To Debit Or Credit", required=True, )
    analytic_precision = fields.Integer(
        string="Analytic Precision", 
        default=100
    )
    analytic_distribution = fields.Json(
        string="Analytic Distribution",
        compute='_compute_analytic_distribution',
        store=True
    )
    
    @api.depends('analytic_account_id')
    def _compute_analytic_distribution(self):
        for record in self:
            if record.analytic_account_id:
                record.analytic_distribution = {
                    str(record.analytic_account_id.id): record.analytic_precision
                }
            else:
                record.analytic_distribution = False


class AccountJournalExpenses(models.Model):
    _inherit = 'account.journal'

    expenses_filtration = fields.Boolean(string="Expenses Filtration")
    for_expenses = fields.Boolean(string="For Expenses")


class AccountMoveExpenses(models.Model):
    _inherit = 'account.move'

    is_expenses = fields.Boolean()
    is_receive = fields.Boolean()
    is_created = fields.Boolean(string="", default=False)
    journal_payment_id = fields.Many2one(comodel_name="account.journal")
    expenses_filtration = fields.Boolean(string="Expenses Filtration", related='journal_payment_id.expenses_filtration')

    @api.model_create_multi
    def create(self, vals_list):
        res = super(AccountMoveExpenses, self).create(vals_list)
        for rec in res:
            if rec.is_expenses:
                partner = self.env['res.partner'].search([('is_expenses', '=', True)], limit=1)
                if not partner:
                    raise ValidationError('Please Add Expenses Partner First')
                rec.partner_id = partner.id
            elif rec.is_receive:
                partner = self.env['res.partner'].search([('is_receive', '=', True)], limit=1)
                if not partner:
                    raise ValidationError('Please Add Receive Partner First')
                rec.partner_id = partner.id
        return res

    def action_post(self):
        res = super(AccountMoveExpenses, self).action_post()
        for rec in self:
            if rec.is_expenses or rec.is_receive:
                if not rec.journal_payment_id:
                    raise ValidationError('Please Select Journal Payment First')
                for line in rec.line_ids:
                    line.date = rec.date
                for line in rec.invoice_line_ids:
                    line.date = rec.date
                self.env['account.payment.register'].with_context(active_model='account.move',
                                                                  active_ids=rec.ids).create(
                    {'journal_id': rec.journal_payment_id.id, 'payment_date': rec.date})._create_payments()
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    expense_line_id = fields.Many2one('expense.line', string="Expense Line")
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account',
        related='expense_line_id.analytic_account_id',
        store=True
    )
    analytic_distribution = fields.Json(
        string="Analytic Distribution",
    )
    analytic_precision = fields.Integer(
        string="Analytic Precision",
        default=100
    )
