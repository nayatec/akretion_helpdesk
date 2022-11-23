# Copyright (C) 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    lead_id = fields.Many2one(string="Lead", comodel_name="crm.lead")
