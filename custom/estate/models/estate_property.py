from odoo import fields, models


class EstateModel(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Fecades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    # 'North', 'South', 'East', 'West'
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('north', 'North'), ('south', 'South'), ('east', 'East'),
                                                     ('west', 'West')],
                                          help='Garden Orientation')

