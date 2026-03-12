# -*- coding: utf-8 -*-
{
    'name': 'Zonaweb Website Template',
    'version': '18.0.1.0.0',
    'category': 'Website',
    'summary': 'Plantilla de sitio web para Zonaweb con sistema de licitaciones',
    'author': 'Zonaweb',
    'website': 'https://www.zonaweb.com',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_sale',
        'mail',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/website_data.xml',
        'views/bidding_request_views.xml',
        'views/website_templates.xml',
        'views/website_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'zonaweb_website/static/src/css/zonaweb_style.css',
            'zonaweb_website/static/src/js/zonaweb_script.js',
        ],
        # ⚠️ El JS del frontend NO debe ir en assets_backend
    },
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 100,
    'images': ['static/description/banner.png'],
}