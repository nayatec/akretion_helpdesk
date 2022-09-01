{
    "name": "Helpdesk REST API",
    "summary": "Add a REST API to create and follow tickets",
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/helpdesk",
    "author": "Akretion, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "helpdesk_mgmt",
        "base_rest",
        "base_rest_abstract_attachment",
    ],
    "external_dependencies": {
        "python": [
            "pydantic",
            "pydantic[email]",
            "extendable_pydantic",
        ]
    },
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_settings.xml",
    ],
}
