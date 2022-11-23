# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    helpdesk_ticket_ids = fields.One2many(
        string="Helpdesk Tickets",
        comodel_name="helpdesk.ticket",
        inverse_name="lead_id",
        help="Linked Helpdesk Tickets to the current Lead",
    )
    helpdesk_ticket_count = fields.Integer(
        "Tickets number", compute="_compute_helpdesk_ticket_count"
    )

    @api.depends("helpdesk_ticket_ids")
    def _compute_helpdesk_ticket_count(self):
        for rec in self:
            rec.helpdesk_ticket_count = len(rec.helpdesk_ticket_ids)

    def action_view_helpdesk_ticket(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "helpdesk_mgmt.helpdesk_ticket_action"
        )
        action["domain"] = [("id", "in", self.helpdesk_ticket_ids.ids)]
        action["context"] = {
            "default_lead_id": self.id,
        }
        if len(self.helpdesk_ticket_ids) == 1:
            action["views"] = [
                (self.env.ref("helpdesk_mgmt.ticket_view_form").id, "form")
            ]
            action["res_id"] = self.helpdesk_ticket_ids.id
        return action
