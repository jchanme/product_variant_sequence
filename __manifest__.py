# -*- coding: utf-8 -*-
{
    'name': "product_variant_sequence",

    'summary': """
        Add handle widge of sequence to the variant list in product template""",

    'description': """
        Add handle widge of sequence to the variant list in product template
    """,

    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
    ],
}
