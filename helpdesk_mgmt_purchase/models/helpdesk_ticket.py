# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    purchase_ids = fields.One2many(
        string="Purchase Orders",
        comodel_name="purchase.order",
        inverse_name="helpdesk_ticket_id",
        help="Linked Purchase Orders to the current Ticket",
    )
    purchase_count = fields.Integer(
        "Purchase Orders number", compute="_compute_purchase_count"
    )

    @api.depends("purchase_ids")
    def _compute_purchase_count(self):
        for rec in self:
            rec.purchase_count = len(rec.purchase_ids)

    def action_view_purchase_order(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "purchase.purchase_form_action"
        )
        action["domain"] = [("id", "in", self.purchase_ids.ids)]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
        }
        if len(self.purchase_ids) == 1:
            action["views"] = [
                (self.env.ref("purchase.purchase_order_form").id, "form")
            ]
            action["res_id"] = self.purchase_ids.id
        return action
