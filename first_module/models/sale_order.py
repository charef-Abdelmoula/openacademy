from odoo import fields, models


class SaleO(models.Model):
    _inherit = 'sale.order'

    # # Add a new column to the res.partner model, by default partners are not
    # # instructors
    # instructor = fields.Boolean("Instructor", default=False)
    #
    # session_ids = fields.Many2many('first_module.session', string="Attended Sessions", readonly=True)
    #
    # instruct = fields.One2many('first_module.session', 'instructor_id', string="instruct")
