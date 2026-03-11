# -*- coding: utf-8 -*-
{
    'name': 'Zonaweb Website Template',
    'version': '18.0.1.0.0',
    'category': 'Website',
    'summary': 'Plantilla de sitio web para Zonaweb con sistema de licitaciones',
    'description': '''
Zonaweb Website Template - Plantilla completa de sitio web con sistema de licitaciones.

Características:
- Página de inicio con carrusel
- Sección de servicios y portafolio
- Sistema de licitaciones integrado
- Formulario de contacto
- Diseño responsive compatible con Odoo 18
    ''',
    'author': 'Zonaweb',
    'website': 'https://www.zonaweb.com',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_sale',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/website_data.xml',
        'demo/demo_data.xml',
        'views/bidding_request_views.xml',
        'views/website_templates.xml',
        'views/website_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'zonaweb_website/static/src/css/zonaweb_style.css',
            'zonaweb_website/static/src/js/zonaweb_script.js',
        ],
        'web.assets_backend': [
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
    'images': ['static/description/banner.png'],
}