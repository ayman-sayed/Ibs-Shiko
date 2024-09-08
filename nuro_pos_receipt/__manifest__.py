# -*- coding: utf-8 -*-
# Part of Nuro Solution Pvt Ltd.
{
    'name': 'POS New Receipt',
    'summary': """Pos Custom Receipt change odoo POS receipt in table format""",
    'description': """
                    Change Odoo POS Receipt
                    Odoo POS Receipt table format
                    New Odoo POS Receipt                                      
                    """,
    'author': "Nurosolution pvt Ltd",
    'category': 'Sales/Point Of Sale',
    'website': 'nurosolution.com',
    'support': 'info@nurosolution.com',
    'company': 'Nurosolution Pvt Ltd',
    'license': 'OPL-1',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'nuro_pos_receipt/static/src/**/*',
        ],
    },
}
