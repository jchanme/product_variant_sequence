# -*- coding: utf-8 -*-
from odoo import http

# class ProductVariantSequence(http.Controller):
#     @http.route('/product_variant_sequence/product_variant_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_variant_sequence/product_variant_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_variant_sequence.listing', {
#             'root': '/product_variant_sequence/product_variant_sequence',
#             'objects': http.request.env['product_variant_sequence.product_variant_sequence'].search([]),
#         })

#     @http.route('/product_variant_sequence/product_variant_sequence/objects/<model("product_variant_sequence.product_variant_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_variant_sequence.object', {
#             'object': obj
#         })
