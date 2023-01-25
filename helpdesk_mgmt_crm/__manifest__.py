# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk CRM",
    "summary": """
        ad a link to crm_lead on helpdesk.ticket.""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt", "sale_crm"],
    "data": [
        # Views
        "views/crm_lead.xml",
        "views/helpdesk_ticket.xml",
    ],
    "demo": [],
}