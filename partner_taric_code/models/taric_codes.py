# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class TaricCodes(models.Model):
    _inherit = 'taric.codes'
    _description = "Add taric codes relation to partner."

    partner_ids = fields.Many2many(
        comodel_name='res.partner', 
        relation='taric_partner_rel',
        string='Partner'
        )