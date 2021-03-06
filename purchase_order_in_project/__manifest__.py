# -*- coding: utf-8 -*-
{
    'name': "purchase_order_in_project",

    'summary': """
        purchase_order_in_project""",

    'description': """
        purchase_order_in_project
    """,

    'author': "Kazushi Eguchi(EnzanTrades Inc,)",
    'website': "https://enzantrades.co.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase.xml',
        'views/project.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
