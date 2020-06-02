# -*- coding: utf-8 -*-
# from odoo import http


# class ContactsAccounting(http.Controller):
#     @http.route('/contacts_accounting/contacts_accounting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacts_accounting/contacts_accounting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacts_accounting.listing', {
#             'root': '/contacts_accounting/contacts_accounting',
#             'objects': http.request.env['contacts_accounting.contacts_accounting'].search([]),
#         })

#     @http.route('/contacts_accounting/contacts_accounting/objects/<model("contacts_accounting.contacts_accounting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacts_accounting.object', {
#             'object': obj
#         })
