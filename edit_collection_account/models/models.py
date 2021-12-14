# -*- coding: utf-8 -*-

from odoo import models, fields, api






class EditAccountMove(models.Model):
    _inherit = 'account.move'

    collection_ids = fields.One2many(comodel_name="collection", inverse_name="move_id", string="Collections", required=False, )


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    next_link_synchronization = fields.Float(string="", required=False, )
    account_online_account_id = fields.Many2one(comodel_name="account.account", string="", required=False, )
    account_online_link_state = fields.Float(string="", required=False, )
    bank_statement_creation_groupby = fields.Float(string="", required=False, )


class Collection(models.Model):
    _name = 'collection'
    _description = 'Collection'

    date = fields.Date(string="Date", required=True, )
    amount = fields.Float(string="Amount",  required=True, )
    move_id = fields.Many2one(comodel_name="account.move", string="Inv", required=False, )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=False,related='move_id.partner_id' )

