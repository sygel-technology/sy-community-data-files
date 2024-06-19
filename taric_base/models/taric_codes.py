# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

class TaricCodes(models.Model):
    _name = 'taric.codes'
    _description = "Mantenance of taric codes."

    code = fields.Char(string='Code', required=True, help='TARIC code.', size=10)
    name = fields.Char(string='Name', required=True, help='TARIC description.', translate=True)
    start_date = fields.Date(string='Start date', required=True, default=fields.Date.context_today, help='Vigence for the TARIC code starts.')
    end_date = fields.Date(string='End date', help='Vigence for the TARIC code ends.')
    hierarchial = fields.Integer(string='Hierarchial', help='Hierarchial value number.')
    company_id = fields.Many2one(comodel_name='res.company', string='Company',
        default=lambda self: self.env.company)

    _sql_constraints = [
                     ('code_unique', 
                      'unique(code)',
                      'Choose another code value - it has to be unique!')
    ]

    @api.onchange('hierarchial')
    def hierarchial_limit(self):
        if self.hierarchial:
            if self.hierarchial <= 0 or self.hierarchial >= 10:
                self.hierarchial = 0
                return {
                    'warning': {
                        'title': 'Hierarchial wrong value',
                        'message': 'Hierarchial must be between 0 and 10.',
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
                
    