from odoo import fields,api,models

class MedicalDoctors(models.Model):
    _name = "medical.doctors"
    _description="record of doctors"

    name=fields.Char(string="Doctor")
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender')