from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'first_module.teacher'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('first_module.course', 'teacher_id', string="Courses")
    # course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
