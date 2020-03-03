from odoo import models, fields, api


class Course(models.Model):
    _name = 'first_module.course'
    _description = "OpenAcademy Courses"
    _inherit = 'mail.thread'
    # _inherit = 'product.template'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    teacher_id = fields.Many2one('first_module.teacher', string="Teacher")

    # the state of the course
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('reset', 'Reset'),
        ('cancel', 'Cancelled'),
    ], required=True, default='draft')

    # calling this function will change the state of the record to done...
    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    def button_reset(self):
        for rec in self:
            rec.state = 'reset'

    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    def copy(self,
             default=None):  # if we make a constraint on the field name to be unique :we can not duplicate =>override the function copy
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    # sql constraints on the course title :must be unique
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
