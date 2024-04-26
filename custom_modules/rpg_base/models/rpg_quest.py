from odoo import fields, models


class DndQuest(models.Model):
    _name = "rpg.quest"
    _description = "This model represents a Quest in Rpg"

    name = fields.Char()

    description = fields.Text()

    potential_reward_item_ids = fields.Many2many(comodel_name="rpg.item")
