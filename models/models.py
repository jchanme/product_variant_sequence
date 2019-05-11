# -*- coding: utf-8 -*-

from odoo import models, fields, api

class many2many_product_variant_sequence(models.Model):
    _inherit = "product.attribute"
    
    sequence = fields.Integer('Sequence', help="Determine the display order")
    attribute_line_ids = fields.many2many('product.attribute.line', 'attribute_id', 'Lines')
