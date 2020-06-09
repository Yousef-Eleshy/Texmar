# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payment_method(models.Model):
    _inherit = 'account.journal'
    
    #Incoming Payment: Bank Account Number
    in_bank_account_number = fields.Char(string='Bank Account Number', readonly=False)
    #Incoming Payment: Visa Number
    in_visa_account_number = fields.Char(string='Visa Account Number', readonly=False)
    #Outgoing Payment: Bank Account Number
    out_bank_account_number = fields.Char(string='Bank Account Number', readonly=False)
    #Outgoing Payment: Visa Number
    out_visa_account_number = fields.Char(string='Visa Account Number', readonly=False)
    
    # Show Incoming Bank Account Number Field IF bank is selected
    @api.depends('inbound_payment_method_ids')
    def _compute_in_bank_payment_method_selected(self):
        for journal in self:
            journal.in_bank_payment_method_selected = any(pm.code == 'bank' for pm in journal.inbound_payment_method_ids)
            
    
    in_bank_payment_method_selected = fields.Boolean(compute='_compute_in_bank_payment_method_selected')
    
    
    # Show Incoming Visa Account Number Field IF visa is selected
    @api.depends('inbound_payment_method_ids')
    def _compute_in_visa_payment_method_selected(self):
        for journal in self:
            journal.in_visa_payment_method_selected = any(pm.code == 'visa' for pm in journal.inbound_payment_method_ids)
            
    
    in_visa_payment_method_selected = fields.Boolean(compute='_compute_in_visa_payment_method_selected')    

    
    
    # Show Outgoing Bank Account Number Field IF bank is selected
    @api.depends('outbound_payment_method_ids')
    def _compute_out_bank_payment_method_selected(self):
        for journal in self:
            journal.out_bank_payment_method_selected = any(pm.code == 'bank' for pm in journal.outbound_payment_method_ids)
            
    
    out_bank_payment_method_selected = fields.Boolean(compute='_compute_out_bank_payment_method_selected')
    
    # Show Outgoing Visa Account Number Field IF visa is selected
    @api.depends('outbound_payment_method_ids')
    def _compute_out_visa_payment_method_selected(self):
        for journal in self:
            journal.out_visa_payment_method_selected = any(pm.code == 'visa' for pm in journal.outbound_payment_method_ids)
            
    
    out_visa_payment_method_selected = fields.Boolean(compute='_compute_out_visa_payment_method_selected')    
