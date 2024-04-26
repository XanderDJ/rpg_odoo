from random import randint

from odoo import fields, models


class DndCampaign(models.Model):
    _name = "rpg.campaign"
    _description = ("A Campaign for Rpg, holds information about the Playable characters"
                    " and is the central piece for deciding which items can be seen on which campaigns")

    name = fields.Char()
    active = fields.Boolean()

    campaign_color = fields.Integer(string="Color", default=lambda x: randint(1, 11))

    rpg_system = fields.Selection([("no_system", "No System")])

