# -*- coding: utf-8 -*-
# from odoo import http


# class AbkOderCustom(http.Controller):
#     @http.route('/abk_oder_custom/abk_oder_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abk_oder_custom/abk_oder_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abk_oder_custom.listing', {
#             'root': '/abk_oder_custom/abk_oder_custom',
#             'objects': http.request.env['abk_oder_custom.abk_oder_custom'].search([]),
#         })

#     @http.route('/abk_oder_custom/abk_oder_custom/objects/<model("abk_oder_custom.abk_oder_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abk_oder_custom.object', {
#             'object': obj
#         })
