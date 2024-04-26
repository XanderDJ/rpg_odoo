from odoo import fields, models


class RpgCreature(models.Model):
    _name = "rpg.creature"
    _description = "Base Rpg Creature (npc mob fiend)"

    name = fields.Char()
    description = fields.Html()

