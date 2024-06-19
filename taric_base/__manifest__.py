# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Taric base',
    'version': '17.0.1.0',
    'author': 'Sygel',
    'website': 'https://www.sygel.es',
    'depends': [
        'base',
    ],
    'data': [
        'security/taric_base_security.xml',
        'security/ir.model.access.csv',
        'views/taric_codes_view.xml',
    ],
}