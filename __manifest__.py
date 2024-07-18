# -*- coding: utf-8 -*-
{
    'name': "dh_delivery_brand_report",

    'summary': """
        Add product_brand in Delivery Note report
        """,

    'description': """
        
    """,

    'author': "Dino Herlambang",
    'website': "http://instagram.com/_dinoherlambang_/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock','product_brand'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
