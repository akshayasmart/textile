{
    'name': "estate",
    'author': "Aiswarya",
    'version': '0.1',
    'depends': ['base','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/status_views.xml',
        'views/category_views.xml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}