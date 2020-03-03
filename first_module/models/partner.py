from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('first_module.session', string="Attended Sessions", readonly=True)

    instruct = fields.One2many('first_module.session', 'instructor_id', string="instruct")

    # count_sessions=fields.Integer("number of sessions",compute="cout_sess")
    # # user_id = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user.id)
    # def count_sess(self):
    #     return  len(self.instruct)
