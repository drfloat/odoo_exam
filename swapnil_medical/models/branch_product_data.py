from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class BranchProduct(models.Model):
    _name = "branch.product.data"
    _description = 'branch product data Module'

    name = fields.Char(string='Branch Name')
    cost = fields.float(string='Branch Cost')
    sale_price = fields.float(string='Branch Sales Price')
    product = fields.Many2one('product.template',string='Product')