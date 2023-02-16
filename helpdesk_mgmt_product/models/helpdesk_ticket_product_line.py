# Copyright 2023 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicketProductLine(models.Model):
    _name = "helpdesk.ticket.product.line"
    _description = "Product line linked to the helpdesk ticket"

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket",
        ondelete="cascade",
    )
    product_id = fields.Many2one(comodel_name="product.product", ondelete="restrict")
    product_tmpl_id = fields.Many2one(comodel_name="product.template", related="product_id.product_tmpl_id",
        readonly=True, store=True)
    product_name = fields.Char(related="product_id.name", readonly=True)
    product_lot_id = fields.Many2one(comodel_name="stock.production.lot", ondelete="restrict")
    product_qty = fields.Float(string="Quantity", digits="Product Unit of Measure")


