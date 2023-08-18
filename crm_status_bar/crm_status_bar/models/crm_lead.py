from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    state = fields.Selection([('work_open', 'Work Open'),
                              ('work_closed', 'Work Closed')], string='State', default='work_open')
    partner_id = fields.Many2one(
        'res.partner', string='Customer')


    # def action_set_visible(self, **additional_values):
    #     """ Lost semantic: probability = 0 or active = False """
    #     res = self.action_archive()
    #     if additional_values:
    #         self.write(dict(additional_values))
    #     return res
