# -*- coding: utf-8 -*-

from odoo import models, fields, api

class many2many_product_variant_sequence(models.Model):
    _inherit = "product.template"

    attribute_line_ids = fields.Many2many('product.attribute.line', 'product_tmpl_id', 'Product Attributes')
