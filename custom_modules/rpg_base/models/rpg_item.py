from odoo import fields, models


class DndItem(models.Model):
    _name = "rpg.item"
    _description = "A Rpg Item"

    name = fields.Char()
    description = fields.Text()
