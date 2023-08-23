from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    state = fields.Selection([('work_open', 'Work Open'),
                              ('work_closed', 'Work Closed')], string='State', default='work_open')
    partner_id = fields.Many2one(
        'res.partner', string='Customer',domain="[('hide_in_contact', '=', False)]")

    regarding_id = fields.Many2one('regarding.regarding', string='Regarding')

    street = fields.Char('Street', compute='_compute_partner_address_values', readonly=True, store=True)
    street2 = fields.Char('Street2', compute='_compute_partner_address_values', readonly=True, store=True)
    zip = fields.Char('Zip', change_default=True, compute='_compute_partner_address_values', readonly=True, store=True)
    city = fields.Char('City', compute='_compute_partner_address_values', readonly=True, store=True)
    state_id = fields.Many2one(
        "res.country.state", string='State',
        compute='_compute_partner_address_values', readonly=True, store=True,
        domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one(
        'res.country', string='Country',
        compute='_compute_partner_address_values', readonly=True, store=True)
    website = fields.Char('Website', index=True, help="Website of the contact", compute="_compute_website",
                          readonly=True, store=True)
    lang_id = fields.Many2one(
        'res.lang', string='Language',
        compute='_compute_lang_id', readonly=True, store=True)
    status_id = fields.Many2one("status.status", string="Status")
    category_id = fields.Many2one("category.category", string="Category")
    last_action = fields.Datetime(string='Last Action')
    quantity = fields.Integer(string='Quantity')

#
# class User(models.Model):
#     _inherit =

