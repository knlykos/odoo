from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class EstatePropertyOfferModel(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float("Price")
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False,
                              default=False)

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(string="Date Deadline", compute="", required=True)

    @api.depends("date_deadline")
    def _compute_date_deadline(self):
        for prop in self:
            date  = prop.create_date.

    def _inverse_validity(self):
        for prop in self:
            if prop.create_date:
                prop.validity = prop.