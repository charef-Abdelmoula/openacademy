from odoo import api, fields, models, exceptions, _


class Prof(models.Model):
    _name = "first_module.prof"
    _description = "Prof"

    # @api.depends('age')
    # def _compute_level_education(self):
    #     # set 'choices' using 'age'
    #     if self.age < 1:
    #         self.choices = "A"
    #     elif (self.age >= 1) and (self.age < 2):
    #         self.choices = "B"
    #     elif (self.age >= 2) and (self.age < 10):
    #         self.choices = "C"
    #     else:
    #         self.choices = "C"

    name = fields.Char(string="Name of prof", required=True)
    description = fields.Text()
    # choices=fields.Selection([('a','A'),('b','B'),('c','C')],string="Choices",compute="_compute_level_education")
    age = fields.Integer(string="Age")
    image = fields.Binary(string="image")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="gender")
    country = fields.Many2one('res.country', string="Nationality")

    # constraint:an age of a teacher  can not be under 20
    @api.constrains('age')
    def _check_something(self):
        if self.age < 20:
            raise exceptions.ValidationError("the age of a prof can't be {}".format(self.age))
    # prof_compute_age=fields.Integer(compute='age_after_ten')
