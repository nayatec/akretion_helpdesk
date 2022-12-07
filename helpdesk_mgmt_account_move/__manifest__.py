# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk account move",
    "summary": """
        Link helpdesk ticket to Client and suuplier invoice).""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt", "account"],
    "data": [
        # Views
        "views/account_move.xml",
        "views/helpdesk_ticket.xml",
    ],
    "demo": [],
}
