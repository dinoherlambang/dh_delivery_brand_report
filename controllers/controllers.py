# -*- coding: utf-8 -*-
# from odoo import http


# class DhDeliveryBrandReport(http.Controller):
#     @http.route('/dh_delivery_brand_report/dh_delivery_brand_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_delivery_brand_report/dh_delivery_brand_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_delivery_brand_report.listing', {
#             'root': '/dh_delivery_brand_report/dh_delivery_brand_report',
#             'objects': http.request.env['dh_delivery_brand_report.dh_delivery_brand_report'].search([]),
#         })

#     @http.route('/dh_delivery_brand_report/dh_delivery_brand_report/objects/<model("dh_delivery_brand_report.dh_delivery_brand_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_delivery_brand_report.object', {
#             'object': obj
#         })
