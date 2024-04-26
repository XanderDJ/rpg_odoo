from odoo import fields, models


class RpgLocation(models.Model):
    _name = "rpg.location"
    _description = (
        "A rpg location, can describe anything really, an inn, a town, a country, ..."
    )

    parent_location_id = fields.Many2one(comodel_name="rpg.location")
    child_location_ids = fields.One2many(
        comodel_name="rpg.location", inverse_name="parent_location_id"
    )

    name = fields.Char()
    description = fields.Html()


