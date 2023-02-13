# -*- coding: utf-8 -*-
# Developed By Hector M. Chavez Cortez

{
    'name': 'Cron Notify',
    'summary': 'Cron Notify',
    'description': 'Create recurring activities with the help of scheduled actions to notify users',
    'author': 'Lucion',
    'website': 'https://lucion.mx',
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/cron_notify_view.xml',
    
    ],
    'application': True,
    'installable': True,
}