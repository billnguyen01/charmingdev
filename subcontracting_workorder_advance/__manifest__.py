# -*- coding: utf-8 -*-
{
    'name': "Subcontracting in Work Orders",

    'summary': """
        Subcontracting in Work Orders""",

    'description': """
        Subcontracting in Work Orders
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Customizations',
    'version': '0.1',

    'depends': ['base', 'mrp', 'purchase', 'sale', 'account', 'stock'],

    'data': [
        'views/component_product_bom.xml',
        'views/mrp_workorder_view.xml'
    ],
}
