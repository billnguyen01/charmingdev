# -*- coding: utf-8 -*-
###################################################################################
#
#    Aboutknowledge (Hong Kong) Limited.
#
#    Copyright (C) 2022-TODAY Aboutknowledge (Hong Kong) Limited (<https://www.cybrosys.com>).
#    Author: Aboutknowledge (Hong Kong) Limited (<https://www.aboutknowledge.com/>)


###################################################################################

{
    'name': 'RMA Process',
    'version': '15.0.1.0.0',
    'summary': """Manages RMA process and credit notes""",
    'description': """This module is used to tracking RMA process and credit note through invoice in sale order.""",
    'category': "Generic Modules/Human Resources",
    'author': 'Aboutknowledge (Hong Kong) Limited',
    'company': 'Aboutknowledge (Hong Kong) Limited',
    'website': "https://www.aboutknowledge.com/",
    'depends': ['base', 'sale_management', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/rma_process.xml',


    ],
    'demo': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}


