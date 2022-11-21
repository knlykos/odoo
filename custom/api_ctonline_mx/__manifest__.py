# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "API CTONLINE.MX",
    'version': '1.0',
    'depends': ['base', 'product'],
    'author': "NKODEX, LLC.",
    'category': 'Sales/CRM',
    'description': 'Module for calling api.ctonline.mx and update on realtime products prices and stocks',
    # data files always loaded at installation
    'data': [
        'views/product_view.xml',
        'views/product_category_views.xml'
        # 'views/estate_property_type_views.xml',
        # 'views/estate_property_tag_views.xml',
        # 'views/estate_property_views.xml',
        # 'views/estate_property_menus.xml',
        # 'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False
}
