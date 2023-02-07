# Copyright 2022 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    product_line_ids = fields.One2many(
        comodel_name="helpdesk.ticket.product.line", inverse_name="ticket_id"
    )
