from odoo import fields, models



class StudentInformation(models.Model):
    _name = 'student.information'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    roll_number = fields.Integer(string='Roll Number', required=True)
    phone = fields.Char(string='Phone')
    father_name = fields.Char(string='Father Name')
    mother_name = fields.Char(string='Mother Name')
    birth_date = fields.Date(string='Birth Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')