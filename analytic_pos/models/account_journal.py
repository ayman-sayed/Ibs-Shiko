# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    ibs_analytic_account = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        help='Analytic account linked to this journal',
    )


