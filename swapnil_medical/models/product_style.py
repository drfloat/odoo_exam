from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductStyle(models.Model):
    _name = 'product.style'
    _description = 'Product Style'

    name = fields.Char(string="style", required=True)
    code = fields.Char(string="Code", required=True, unique=True)
    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'Code already present')]
    # @api.constrains('code')
    # def _check_child_age(self):
    #     for rec in self:
    #         if rec.code:
    #             for res in rec.code:
    #                 for rep in rec.code:
    #                     if res==rec:
    #                         raise ValidationError(_("code should be unique"))


    @api.constrains('code')
    def _check_unique_code(self):
        for record in self:
            if self.search_count([('code', '=', record.code)]) > 1:
                raise ValidationError(_("Code should be unique"))




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