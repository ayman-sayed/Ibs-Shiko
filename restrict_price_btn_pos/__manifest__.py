{
    'name': 'Restrict Price Button In POS',
    'version': '13.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': """This module is used to restrict button based on user""",
    'description': 'Pos buttons can be restricted to the users.Buttons is '
                   'restricted if we enable the fields in res user.',
    'author': '',
    'website': '',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_users_views.xml',
    ],
    'qweb': [
        'static/src/xml/price_button.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
