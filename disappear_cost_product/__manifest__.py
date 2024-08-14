{
    "name": "Disappear Cost Product",
    "version": "14.0.0.1.0",
    "author": "Ibs",
    "category": "Product",
    "summary": "add record in group disappear cost in model product",
    "description": """
        add record in group disappear cost in model product
    """,
    "depends": [
        "product",
    ],
    "data": [
        "security/security_view.xml",
        "views/cost_product_template_view.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
