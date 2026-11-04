from odoo import api, fields, models



class OtherSchoolHistory(models.Model):
    _name = 'other.school.history'
    _description = 'Other School History'

    name = fields.Char(string="Name", required=True)






class StudentSchoolHistory(models.Model):
    _name = 'student.school.history'
    _description = 'Student School History'

    student_id = fields.Many2one('student.information')
    other_school_id = fields.Many2one('other.school.history', string="Other School", required=True)
    passing_year = fields.Char(string="Passing Year", required=True)
    class_name = fields.Char(string="Class Name", required=True)