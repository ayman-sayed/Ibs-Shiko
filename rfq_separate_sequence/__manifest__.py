# -*- encoding: utf-8 -*-
{
    'name' : 'SW - RFQ Separate Sequence',
    'category' : 'Purchase',
    'author' : 'Smart Way Business Solutions',
    'website' : 'https://www.smartway.co',
    'license':  "Other proprietary",
    'summary': """Add a special sequence to your RFQs""",
    'data': ['sequence.xml','view.xml'],
    'depends' : ['base', 'purchase','stock'],
    'images':  ["static/description/image.png"],
    'installable': True,
    'auto_install': False,
}