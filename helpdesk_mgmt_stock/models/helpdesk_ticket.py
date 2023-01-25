# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    stock_picking_ids = fields.One2many(
        string="Stock Picking",
        comodel_name="stock.picking",
        inverse_name="helpdesk_ticket_id",
        help="Linked stock picking to the current Ticket",
    )
    stock_picking_out_ids = fields.One2many(
        string="Stock Picking out",
        comodel_name="stock.picking",
        compute="_compute_stock_picking_count",
        help="Linked Stock Picking out to the current Ticket",
    )
    stock_picking_in_ids = fields.One2many(
        string="Stock Picking in",
        comodel_name="stock.picking",
        compute="_compute_stock_picking_count",
        help="Linked Stock Picking in to the current Ticket",
    )
    stock_picking_out_count = fields.Integer(
        "Stock Picking out number", compute="_compute_stock_picking_count"
    )
    stock_picking_in_count = fields.Integer(
        "Stock Picking in number", compute="_compute_stock_picking_count"
    )

    @api.depends(
        "stock_picking_ids",
    )
    def _compute_stock_picking_count(self):
        for rec in self:
            rec.stock_picking_out_ids = rec.stock_picking_ids.filtered(
                lambda l: l.picking_type_id.code == "outgoing"
            )
            rec.stock_picking_in_ids = rec.stock_picking_ids.filtered(
                lambda l: l.picking_type_id.code == "incoming"
            )
            rec.stock_picking_out_count = len(rec.stock_picking_out_ids)
            rec.stock_picking_in_count = len(rec.stock_picking_in_ids)

    def action_view_stock_picking_out(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.action_picking_tree_all"
        )
        action["domain"] = [
            ("id", "in", self.stock_picking_out_ids.ids),
        ]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
            "contact_display": "partner_address",
        }
        if len(self.stock_picking_out_ids) == 1:
            action["views"] = [(self.env.ref("stock.view_picking_form").id, "form")]
            action["res_id"] = self.stock_picking_out_ids.id
        return action

    def action_view_stock_picking_in(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.action_picking_tree_all"
        )
        action["domain"] = [("id", "in", self.stock_picking_in_ids.ids)]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
            "contact_display": "partner_address",
        }
        if len(self.stock_picking_in_ids) == 1:
            action["views"] = [(self.env.ref("stock.view_picking_form").id, "form")]
            action["res_id"] = self.stock_picking_in_ids.id
        return action
