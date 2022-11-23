# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import tagged
from odoo.tests.common import users

from . import common

EMPLOYEE = "user_employee"


@tagged("post_install")
class Test(common.TestDS):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls._get_user(
            cls,
            login=EMPLOYEE,
            groups="sales_team.group_sale_salesman_all_leads, helpdesk_mgmt.group_helpdesk_manager",
        )
        helpdesk_ticket_vals, lead_vals = [], []
        for helpdesk_ticket in (
            "ticket 1",
            "ticket 2",
        ):
            helpdesk_ticket_vals.append(
                {"name": helpdesk_ticket, "description": helpdesk_ticket}
            )
        cls.helpdesk_tickets = cls.env["helpdesk.ticket"].create(helpdesk_ticket_vals)
        for lead in ("lead 1", "lead 2", "lead 3"):
            lead_vals.append(
                {"name": lead, "partner_id": cls.env.ref("base.res_partner_2").id}
            )
        cls.leads = cls.env["crm.lead"].create(lead_vals)
        cls.helpdesk_tickets_lead_1 = cls.helpdesk_tickets.filtered(
            lambda s: s.name in ("ticket 1", "ticket 2")
        )

        cls.lead_1 = cls.leads.filtered(lambda s: s.name == "lead 1")
        cls.helpdesk_ticket_1 = cls.helpdesk_tickets.filtered(
            lambda s: s.name == "ticket 1"
        )
        cls.helpdesk_ticket_2 = cls.helpdesk_tickets.filtered(
            lambda s: s.name == "ticket 2"
        )

    @users(EMPLOYEE)
    def test_attache_helpdesk_tickets_to_leads(self):
        self.assertEqual(self.lead_1.helpdesk_ticket_count, 0)
        self.helpdesk_ticket_1.lead_id = self.lead_1
        self.assertEqual(self.lead_1.helpdesk_ticket_ids, self.helpdesk_ticket_1)
        self.assertEqual(self.lead_1.helpdesk_ticket_count, 1)
        self.helpdesk_ticket_2.lead_id = self.lead_1
        self.assertEqual(self.lead_1.helpdesk_ticket_count, 2)
        self.assertEqual(self.lead_1.helpdesk_ticket_ids, self.helpdesk_tickets_lead_1)
