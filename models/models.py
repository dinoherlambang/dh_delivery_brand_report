from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_id = fields.Many2one(related='product_id.product_brand_id', string='Brand', store=True)
