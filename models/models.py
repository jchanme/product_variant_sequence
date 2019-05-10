# -*- coding: utf-8 -*-

from odoo import models, fields, api

class many2many_product_variant_sequence(models.Model):
    _name = 'product.variant.handle'
    _description = 'Model for many2many (handle)'
    _order = 'sequence'
    name = fields.Char('Naam')
    sequence = fields.Integer('sequence', help="Sequence for the handle.",default=10)
