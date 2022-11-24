# Copyright 2022 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    product_line_ids = fields.One2many(
        comodel_name="helpdesk.ticket.product.line", inverse_name="ticket_id"
    )


class HelpdeskTicketProductLine(models.Model):
    _name = "helpdesk.ticket.product.line"
    _description = "Product line linked to the helpdesk ticket"

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket",
    )
    product_id = fields.Many2one(comodel_name="product.product")
    product_name = fields.Char(related="product_id.name", readonly=True)
    product_lot_id = fields.Many2one(comodel_name="stock.production.lot")
    product_qty = fields.Float(string="Quantity", digits="Product Unit of Measure")
