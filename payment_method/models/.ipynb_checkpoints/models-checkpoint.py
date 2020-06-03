# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payment_method(models.Model):
    _inherit = 'account.journal'
    
    bank_account_number = fields.text(string='Account Number', readonly=False)
