from odoo import fields, models

class Invoice_mod(models.Model):
    _inherit = 'account.move'

    session_id = fields.Many2one("first_module.session", string="session")