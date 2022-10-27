# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "NKODEX, LLC.",
    'category': 'Sales/CRM',
    'description': 'Description Real State Module',
    # data files always loaded at installation
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False
}
