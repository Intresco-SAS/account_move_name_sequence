from odoo import api, fields, models

class AccountPayment(models.Model):

    _inherit = 'account.payment'

    payment_type = fields.Selection([('outbound', 'Send Money'), ('inbound', 'Receive Money')], 
                                    string='Payment Type',
                                    readonly=True
    )
    