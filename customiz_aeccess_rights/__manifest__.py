{
    'name': "Customize Access Rights",
    'author': "IDigiMeta",
    'version': '14.0',
    "category":'Groups/Access Rights',
    "summary": "Managing User Groups and Access Rights",
    "description":
        "This custom module has four groups with different access levels admin, user, manager, and operator head Rights.",
    'depends': ['base', 'crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
