# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk stock picking",
    "summary": """
        Link helpdesk ticket to stock picking).""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt", "stock"],
    "data": [
        # Views
        "views/stock_picking.xml",
        "views/helpdesk_ticket.xml",
    ],
    "demo": [],
}
