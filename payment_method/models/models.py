# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payment_method(models.Model):
    _inherit = 'account.journal'
    
    in_bank_account_number = fields.Char(string='Bank Account Number', readonly=False)
    
    in_visa_account_number = fields.Char(string='Visa Account Number', readonly=False)
    
    out_bank_account_number = fields.Char(string='Bank Account Number', readonly=False)
    
    out_visa_account_number = fields.Char(string='Visa Account Number', readonly=False)

