# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

class TaricCode(models.Model):
    _name = 'taric.code'
    _description = "Maintenance of TARIC codes."

    code = fields.Char(string='Code', required=True, help='TARIC code. Must have 10 dígits.')
    name = fields.Char(string='Name', required=True, help='TARIC description.', translate=True)
    start_date = fields.Date(string='Start date', required=True, default=fields.Date.context_today, help='Vigence for the TARIC code starts.')
    end_date = fields.Date(string='End date', help='Vigence for the TARIC code ends.')
    hierarchical = fields.Integer(string='Hierarchical', help='Hierarchical value number.')
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
        default=lambda self: self.env.company)

    _sql_constraints = [
                     ('code_unique', 
                      'unique(code)',
                      'Choose another code value - it has to be unique!')
    ]

    @api.onchange('hierarchical')
    def hierarchical_limit(self):
        if self.hierarchical:
            if self.hierarchical <= 0 or self.hierarchical >= 10:
                self.hierarchical = 0
                return {
                    'warning': {
                        'title': 'Hierarchical wrong value',
                        'message': 'Hierarchical must be between 0 and 10.',
                    }
                }
                
    

    @api.onchange('end_date')
    def end_date_validate(self):
        if self.end_date:
            if self.end_date < self.start_date:
                self.end_date = self.start_date
                return {
                    'warning': {
                        'title': 'End date wrong value',
                        'message': 'End date must be bigger than start date.',
                    }
                }
                
    