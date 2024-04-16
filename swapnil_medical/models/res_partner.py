from odoo import models, fields,api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    customer_rating = fields.Selection(related='partner_id.priority', string="Customer Rating")







