# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")


class Courses(models.Model):
    _inherit = 'product.template'

    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
    course_term = fields.Selection([
    ('1', "1 day"),
    ('2', "2 days"),
    ('3', "3 days"),
    ('4', "4 days"),
    ('5', "5 days"),
])
