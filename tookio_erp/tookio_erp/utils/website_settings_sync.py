import frappe


def sync_tookio_nav_footer():
    """Rewrite Website Settings navbar and footer links to match Tookio pages."""
    ws = frappe.get_doc("Website Settings", "Website Settings")

    top_bar_items = [
        {"label": "ERPNext", "url": "/erpnext", "right": 1},
        {"label": "ARC System", "url": "/arc-system", "right": 1},
        {"label": "Automation & AI", "url": "/automation-hub", "right": 1},
        {"label": "Custom Development", "url": "/custom-development", "right": 1},
        {"label": "Resources", "url": "", "right": 1},
        {"label": "Blog", "url": "/blog", "parent_label": "Resources", "right": 1},
        {"label": "Case Studies", "url": "/case-studies", "parent_label": "Resources", "right": 1},
        {"label": "About", "url": "/about", "parent_label": "Resources", "right": 1},
        {"label": "Privacy Policy", "url": "/privacy-policy", "parent_label": "Resources", "right": 1},
        {"label": "Terms", "url": "/terms", "parent_label": "Resources", "right": 1},
        {"label": "Pricing", "url": "/pricing", "right": 1},
        {"label": "Contact", "url": "/contact", "right": 1},
    ]

    footer_items = [
        {"label": "Services", "parent_label": None, "url": None, "right": 0},
        {"label": "ERPNext Solutions", "parent_label": "Services", "url": "/erpnext", "right": 0},
        {"label": "n8n Automation", "parent_label": "Services", "url": "/automation-hub", "right": 0},
        {"label": "ARC Compliance", "parent_label": "Services", "url": "/arc-system", "right": 0},
        {"label": "Custom Development", "parent_label": "Services", "url": "/custom-development", "right": 0},
        {"label": "Resources", "parent_label": None, "url": None, "right": 0},
        {"label": "Blog", "parent_label": "Resources", "url": "/blog", "right": 0},
        {"label": "Case Studies", "parent_label": "Resources", "url": "/case-studies", "right": 0},
        {"label": "Pricing", "parent_label": "Resources", "url": "/pricing", "right": 0},
        {"label": "Privacy Policy", "parent_label": "Resources", "url": "/privacy-policy", "right": 0},
        {"label": "Terms", "parent_label": "Resources", "url": "/terms", "right": 0},
        {"label": "Company", "parent_label": None, "url": None, "right": 0},
        {"label": "About", "parent_label": "Company", "url": "/about", "right": 0},
        {"label": "Contact", "parent_label": "Company", "url": "/contact", "right": 0},
        {"label": "For Enterprises", "parent_label": "Company", "url": "/for-enterprises", "right": 0},
        {"label": "Get Started", "parent_label": None, "url": None, "right": 0},
        {"label": "Free Consultation", "parent_label": "Get Started", "url": "/contact", "right": 0},
        {"label": "Demo Request", "parent_label": "Get Started", "url": "/contact", "right": 0},
        {"label": "Pricing Guide", "parent_label": "Get Started", "url": "/pricing", "right": 0},
        {"label": "Contact", "parent_label": "Get Started", "url": "/contact", "right": 0},
    ]

    ws.set("top_bar_items", [])
    ws.set("footer_items", [])

    for item in top_bar_items:
        ws.append("top_bar_items", item)

    for item in footer_items:
        ws.append("footer_items", item)

    ws.save(ignore_permissions=True)
    frappe.db.commit()

    return {
        "updated": True,
        "top_bar_count": len(ws.top_bar_items),
        "footer_count": len(ws.footer_items),
    }
