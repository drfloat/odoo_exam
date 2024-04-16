from odoo import fields,api,models

class Partner(models.Model):
    _description = 'Contact'
    _inherit = 'res.partner'

    priority = fields.Selection([('0', 'Medium'), ('1', 'Very Low'), ('2', 'Medium'), ('3', 'Normal'), ('4', 'High'), ('5', 'Very High')], default='1', index=True)