# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    account_move_out_ids = fields.One2many(
        string="Client invoice",
        comodel_name="account.move",
        inverse_name="helpdesk_ticket_id",
        help="Linked Client invoice to the current Ticket",
        domain="[('move_type', 'in', ('out_invoice','out_refund'))]",
    )
    account_move_in_ids = fields.One2many(
        string="Supplier invoice",
        comodel_name="account.move",
        inverse_name="helpdesk_ticket_id",
        help="Linked Supplier invoice to the current Ticket",
        domain="[('move_type', 'in', ('in_invoice','in_refund'))]",
    )
    account_move_out_count = fields.Integer(
        "Client invoice number", compute="_compute_account_move_count"
    )
    account_move_in_count = fields.Integer(
        "Supplier invoice number", compute="_compute_account_move_count"
    )

    @api.depends("account_move_out_ids", "account_move_in_ids")
    def _compute_account_move_count(self):
        for rec in self:
            rec.account_move_out_count = len(rec.account_move_out_ids)
            rec.account_move_in_count = len(rec.account_move_in_ids)

    def action_view_account_move_out(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "account.action_move_out_invoice_type"
        )
        action["domain"] = [("id", "in", self.account_move_out_ids.ids)]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
        }
        if len(self.account_move_ids) == 1:
            action["views"] = [(self.env.ref("account.view_move_form").id, "form")]
            action["res_id"] = self.account_move_out_ids.id
        return action

    def action_view_account_move_in(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "account.action_move_in_invoice_type"
        )
        action["domain"] = [("id", "in", self.account_move_in_ids.ids)]
        action["context"] = {
            "default_helpdesk_ticket_id": self.id,
        }
        if len(self.account_move_ids) == 1:
            action["views"] = [(self.env.ref("account.view_move_form").id, "form")]
            action["res_id"] = self.account_move_in_ids.id
        return action
