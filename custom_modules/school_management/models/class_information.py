from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = 'class.information'
    _description = 'Class Information'

    name = fields.Char(string="Class Name")
    class_teacher_id = fields.Many2one('res.partner', string="Class Teacher", required=True)
    number_of_seats = fields.Integer(string="Number of Seats", required=True)
    