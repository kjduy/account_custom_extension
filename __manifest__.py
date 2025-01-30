# -*- coding: utf-8 -*-

{
    'name': 'Account Custom Extension',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'Accounting extension with customized reports.',
    'author': 'Kevin Duy',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/invoice_report.xml',
        'views/invoice_report_template.xml',
    ],
    'license': 'LGPL-3'
}
