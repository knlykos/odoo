from odoo import api, fields, models, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ct_code = fields.Char(string='CT Code')
