# -*- coding: utf-8 -*-
{
    'name': 'Tema Zonaweb',
    'version': '18.0.1.0.0',
    'category': 'Theme/Corporate',
    'summary': 'Tema corporativo profesional para Zonaweb',
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
        'views/website_templates.xml',
        'views/bidding_request_views.xml',
        'views/website_menu.xml',
        'data/website_data.xml',
    ],
    'assets': {
        'website.assets_frontend': [
            'zonaweb_website/static/src/css/zonaweb_style.css',
            'zonaweb_website/static/src/js/zonaweb_script.js',
        ],
    },
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 100,
    'images': [
        'static/description/banner.png',
        'static/description/theme_preview.png',
    ],
}