# -*- coding: utf-8 -*-
# from odoo import http


# class AbkContactCustom(http.Controller):
#     @http.route('/abk_contact_custom/abk_contact_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abk_contact_custom/abk_contact_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abk_contact_custom.listing', {
#             'root': '/abk_contact_custom/abk_contact_custom',
#             'objects': http.request.env['abk_contact_custom.abk_contact_custom'].search([]),
#         })

#     @http.route('/abk_contact_custom/abk_contact_custom/objects/<model("abk_contact_custom.abk_contact_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abk_contact_custom.object', {
#             'object': obj
#         })
