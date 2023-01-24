# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    helpdesk_ticket_id = fields.Many2one(
        string="Tickets", comodel_name="helpdesk.ticket",
        groups="helpdesk_mgmt.group_helpdesk_user_own",
    )
