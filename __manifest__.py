# -*- coding: utf-8 -*-
{
    'name': "Academia",

    'summary': """
        Gestionar una academia de inglés""",

    'description': """
        Gestionar una academia de inglés, alumnos, cursos y profesores
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'security/security.xml'
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_curso_alumno.xml',
        'reports/report_alumno_notas.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
