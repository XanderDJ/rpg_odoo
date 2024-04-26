# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    "name": "rpg_base",
    "summary": """
        Implement Rpg System in Odoo
        """,
    "description": """
        Implementation of Rpg system in odoo. Allows for players, maps, items, lore,...
    """,
    "author": "Xander De Jaegere",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Rpg",
    "version": "17.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": ["security/ir.model.access.csv", "security/groups.xml"],
    # only loaded in demonstration mode
    "demo": [],
}
