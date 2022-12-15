# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    helpdesk_ticket_id = fields.Many2one(
        string="Tickets", comodel_name="helpdesk.ticket"
    )
