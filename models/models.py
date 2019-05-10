# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class product_variant_sequence(models.Model):
#     _name = 'product_variant_sequence.product_variant_sequence'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
