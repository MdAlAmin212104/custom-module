from odoo import fields, models



class StudentInformation(models.Model):
    _name = 'student.information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True, tracking=True)
    roll_number = fields.Integer(string='Roll Number', required=True, tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    father_name = fields.Char(string='Father Name', tracking=True)
    mother_name = fields.Char(string='Mother Name', tracking=True)
    birth_date = fields.Date(string='Birth Date', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    address = fields.Text(string='Address', tracking=True)


    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], default='draft', string='Status', tracking=True)


    previous_record_ids = fields.One2many('student.school.history', 'student_id', string='Previous School Records') 

    image = fields.Binary(string='Image')
    student_documents_ids = fields.Many2many('ir.attachment', string='Student Documents')
    student_notes = fields.Text(string='Student Notes')


    def confirm_student(self):

        for record in self:
            if record.status == 'draft':
                record.status = 'confirmed'

    def reset_to_draft(self):

        for record in self:
            if record.status == 'confirmed':
                record.status = 'draft'