# Copyright 2023 Akretion (https://www.akretion.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ticket_product_line_ids = fields.One2many(
        string="Ticket Product Line",
        comodel_name="helpdesk.ticket.product.line",
        inverse_name="product_tmpl_id",
        help="Linked Ticket Product Line to the current Product",
    )
    ticket_product_line_count = fields.Integer(
        "Ticket Product number", compute="_compute_ticket_product_line_count"
    )

    @api.depends("ticket_product_line_ids")
    def _compute_ticket_product_line_count(self):
        for rec in self:
            rec.ticket_product_line_count = len(rec.ticket_product_line_ids)

    def action_view_ticket_product_line(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "helpdesk_mgmt_product.action_helpdesk_ticket_product_line_tree"
        )
        action["domain"] = [('product_id.product_tmpl_id', 'in', self.ids)]
        return action


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_view_ticket_product_line(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "helpdesk_mgmt_product.action_helpdesk_ticket_product_line_tree"
        )
        action["domain"] = [('product_id', 'in', self.ids)]
        return action
