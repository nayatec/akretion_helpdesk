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
            groups="purchase.group_purchase_user, helpdesk_mgmt.group_helpdesk_manager",
        )
        helpdesk_ticket_ids, purchase_ids = [], []
        for helpdesk_ticket in (
            "ticket 1",
            "ticket 2",
        ):
            helpdesk_ticket_ids.append(
                {"name": helpdesk_ticket, "description": helpdesk_ticket}
            )
        cls.helpdesk_tickets = cls.env["helpdesk.ticket"].create(helpdesk_ticket_ids)
        for purchase in ("purchase 1", "purchase 2", "purchase 3"):
            purchase_ids.append(
                {"name": purchase, "partner_id": cls.env.ref("base.res_partner_2").id}
            )
        cls.purchases = cls.env["purchase.order"].create(purchase_ids)
        cls.purchases_helpdesk_ticket_2 = cls.purchases.filtered(
            lambda s: s.name in ("purchase 2", "purchase 3")
        )

        cls.purchase_1 = cls.purchases.filtered(lambda s: s.name == "purchase 1")
        cls.purchase_2 = cls.purchases.filtered(lambda s: s.name == "purchase 2")
        cls.purchase_3 = cls.purchases.filtered(lambda s: s.name == "purchase 3")
        cls.helpdesk_ticket_1 = cls.helpdesk_tickets.filtered(
            lambda s: s.name == "ticket 1"
        )
        cls.helpdesk_ticket_2 = cls.helpdesk_tickets.filtered(
            lambda s: s.name == "ticket 2"
        )

    @users(EMPLOYEE)
    def test_attache_helpdesk_tickets_to_purchases(self):
        self.assertEqual(
            self.helpdesk_ticket_1.purchase_ids, self.env["purchase.order"]
        )
        self.assertEqual(self.helpdesk_ticket_1.purchase_count, 0)
        self.purchase_1.helpdesk_ticket_id = self.helpdesk_ticket_1
        self.assertEqual(self.helpdesk_ticket_1.purchase_ids, self.purchase_1)
        self.assertEqual(self.helpdesk_ticket_1.purchase_count, 1)
        self.purchase_2.helpdesk_ticket_id = self.helpdesk_ticket_2
        self.purchase_3.helpdesk_ticket_id = self.helpdesk_ticket_2
        self.assertEqual(self.helpdesk_ticket_2.purchase_count, 2)
        self.assertEqual(
            self.helpdesk_ticket_2.purchase_ids, self.purchases_helpdesk_ticket_2
        )
