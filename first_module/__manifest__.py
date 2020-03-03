# -*- coding: utf-8 -*-
{
    'name': "first_module",

    'summary': """Open Academy BY CHAREF""",

    'description': """
        Manage Your shool easilly
    """,

    'author': "My Company",
    'website': "http://www.charefabdo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'board'],

    # any module necessary for this one to work correctly

    # always loaded
    'data': [
        # 'security/security.xml',
        'views/views.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/reports.xml',
        'views/session_board.xml',
        'views/prof.xml',
        'views/data.xml',
        'demo/demo_teacher.xml',
        'views/teach_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
