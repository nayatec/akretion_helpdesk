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

    stock_picking_count = fields.Integer(
        "Stock Picking number", compute="_compute_stock_picking_count"
    )

    @api.depends("stock_picking_ids", )
    def _compute_stock_picking_count(self):
        for rec in self:
            rec.stock_picking_count = len(rec.stock_picking_ids)

    def action_view_stock_picking(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "stock.action_picking_tree_all"
        )
        action["domain"] = [("id", "in", self.stock_picking_ids.ids),
                            ('picking_type', 'in', ('out_invoice', 'out_refund'))]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
            'contact_display': 'partner_address',
        }
        if len(self.stock_picking_ids) == 1:
            action["views"] = [(self.env.ref("stock.view_picking_form").id, "form")]
            action["res_id"] = self.stock_picking_ids.id
        return action
