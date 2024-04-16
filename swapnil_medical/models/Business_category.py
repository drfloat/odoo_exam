from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class BusinessCategory(models.Model):
    _name = 'business.category'
    _description = 'business category'

    name = fields.Char(string="style", required=True)




class Product(models.Model):
    _inherit = 'product.product'

    style_id = fields.Many2one('product.style', string="Product Style")




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    name = fields.Many2one('product.style', string="Product Style",related='product_id.style_id')

@api.onchange('product_id')
def onchange_product_id(self):
    if self.product_id:
        self.product_style_id = self.product_id.style_id.id