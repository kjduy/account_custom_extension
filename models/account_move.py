# -*- coding: utf-8 -*-

import hashlib

from odoo import models, fields, api, _
from odoo.tools import format_amount


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_risk_level = fields.Selection([
        ('low', _('Low Risk')),
        ('medium', _('Moderate Risk')),
        ('high', _('High Risk'))
    ], compute='_compute_invoice_analysis', store=True, string=_("Invoice Risk Level"))
    unique_invoice_identifier = fields.Char(
        compute='_compute_invoice_analysis', store=True, string=_("Unique Invoice Identifier")
    )
    invoice_reference_number = fields.Integer(string=_("Invoice Reference Number"))
    is_special_invoice = fields.Boolean(default=False, string=_("Is Special Invoice?"))
    account_payment_term = fields.Many2one('account.payment.term', string=_("Account Payment Term"))
    customer_contact = fields.Many2one('res.partner', string=_("Customer Contact"))

    @api.depends('amount_total', 'state', 'currency_id')
    def _compute_invoice_analysis(self):
        for record in self:
            currency = record.currency_id or self.env.company.currency_id
            total_formatted = format_amount(self.env, record.amount_total, currency)
            if record.amount_total < 500:
                risk = 'low'
                risk_label = _('Low Risk')
            elif record.amount_total <= 2000:
                risk = 'medium'
                risk_label = _('Moderate Risk')
            else:
                risk = 'high'
                risk_label = _('High Risk')
            record.invoice_risk_level = risk
            unique_str = f"{record.id}{record.amount_total}{record.invoice_date}"
            unique_hash = hashlib.md5(unique_str.encode()).hexdigest()[:10]
            record.unique_invoice_identifier = _("INV-%s") % unique_hash.upper()
