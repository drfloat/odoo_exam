import datetime

from odoo import api,fields,models

class MedicalPatients(models.Model):
    _name = "medical.patient"
    #_inherit = ""
    _description= "Record of medical patients"


    name = fields.Char(string="Name",required="True",tracking=True)
    address = fields.Char(string="City")
    is_member = fields.Boolean(string="Membership",tracking=True)
    medicines = fields.Char(string="Medicines")
    bill= fields.Integer(string="Bill of Items",tracking=True)
    total_bill= fields.Integer(string="Total Bill",compute="Discount_Calculator")
    doctors=fields.Many2one('medical.doctors',string="Doctors")
    date=fields.Char(string="Date")

    @api.depends('bill')
    def Discount_Calculator(self):
        for rec in self:
            if rec.bill and rec.is_member:
                if rec.is_member == True:
                    rec.total_bill = rec.bill*0.75
                else:
                    rec.total_bill = rec.bill
            else:
                rec.total_bill=0




