# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_


class Student(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'school.student'
    # python-inherited models

    # the model's informal name
    _description = 'Student Record'
    # default order field for searching results
    _order = 'name'



    name = fields.Char(string='Name', required=True, track_visibility=True)
    age = fields.Integer(string='Age', track_visibility=True)
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='Gender')
