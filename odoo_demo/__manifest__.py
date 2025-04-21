# -*- coding: utf-8 -*-
{
    'name': 'Odoo Demo',
    'version': '1.0.0',
    'summary': """ Odoo Demo Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web', 'contacts'],
    "data": [
        "views/menus.xml"
    ],
    'assets': {
              'web.assets_backend': [
                  'odoo_demo/static/src/**/*'
              ],
          },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
