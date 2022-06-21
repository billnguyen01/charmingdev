# -*- coding: utf-8 -*-
{
    'name': 'Report Custom',
    'summary': 'Report Customization',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'category': 'Inventory/Purchase',
    'author': 'Vishal',
    'support': 'vvgediya@gmail.com',
    'depends': [
        'base', 'purchase', 'abk_contact_custom'
    ],
    'data': [
        'views/purchase_order_views.xml',
        'report/external_layout_custom.xml',
        'report/purchase_order_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
