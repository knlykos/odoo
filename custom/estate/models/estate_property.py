from odoo import fields, models, api


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

    # Special
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean("Active", default=True)

    property_type_id = fields.Many2one("estate.property.id", string="Estate Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offer")
    total_area = fields.Integer(string="Total Area", compute="_compute_total_area")
    best_price = fields.Integer(string="Best Offer", compute="_compute_best_price")

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        for prop in self:
            if prop.offer_ids:
                prop.best_price = max(prop.offer_ids.mapped("price"))
            else:
                prop.best_price = 0.0
