from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    color = fields.Char(string="Color")
    branch_product_data_id = fields.One2many('branch.product.data', string='Business Category')