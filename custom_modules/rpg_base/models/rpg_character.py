from odoo import fields, models


class RpgCharacter(models.Model):
    _name = "rpg.character"
    _description = (
        "A playable character in a campaign setting, can also be used to create some more interesting"
        " npcs"
    )

    name = fields.Char()
    description = fields.Text()

    current_location_id = fields.Many2one(comodel_name="rpg.location")
