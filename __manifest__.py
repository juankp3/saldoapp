# -*- coding: utf-8 -*-
{
    'name': "saldoapp",

    'summary': """
        Aplicación que le permitirá a tus usuarios gestionar sus ingresos y egresos
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Juan Kuga",
    'website': "https://perfecciondigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/records_movimiento.xml',
        'data/categoria.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}