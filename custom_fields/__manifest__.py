#    Aboutknowledge (Hong Kong) Limited.
#
#    Copyright (C) 2022-TODAY Aboutknowledge (Hong Kong) Limited (<https://www.cybrosys.com>).
#    Author: Aboutknowledge (Hong Kong) Limited (<https://www.aboutknowledge.com/>)


###################################################################################


{
    'name': 'Sales Custom Fields',
    'version': '15.0.1.0.0',
    'summary': """Custom fields addition in sale order form.""",
    'description': """This module is used to add custom fields in sale order form view""",
    'category': "Generic Modules/Human Resources",
    'author': 'Aboutknowledge (Hong Kong) Limited',
    'company': 'Aboutknowledge (Hong Kong) Limited',
    'website': "https://www.aboutknowledge.com/",
    'depends': ['base', 'sale', 'purchase', 'product'],
    'auto_install': False,
    'application': False,
    'installable': True,
    'data': [
            'views/sale_order.xml',
            'views/product_template.xml'
            ]
}
