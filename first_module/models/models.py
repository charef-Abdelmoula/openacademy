# -*- coding: utf-8 -*-

from odoo import models, fields, api


class first_module(models.Model):
     _name = 'first_module.first_module'
     _description = 'first module By Charef Abdelmoula'
#     _description = 'first_module.first_module'
     #_rec_name='title' if changed the important field name by title for example


     name = fields.Char(string="Title ",required=True,help="Name") #attribut
     #name is an important field

     description =fields.Text()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
