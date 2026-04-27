import frappe
import json

def fix_all():
    # Website Settings
    ws = frappe.get_doc("Website Settings", "Website Settings")
    ws.top_bar_items = []
    
    ws.append("top_bar_items", {"label": "Home", "url": "/home"})
    ws.append("top_bar_items", {"label": "Services", "url": ""})
    ws.append("top_bar_items", {"label": "ERPNext", "url": "/services", "parent_label": "Services"})
    ws.append("top_bar_items", {"label": "ARC System", "url": "/arc-system", "parent_label": "Services"})
    ws.append("top_bar_items", {"label": "Automation", "url": "/automation-hub", "parent_label": "Services"})
    
    ws.append("top_bar_items", {"label": "Resources", "url": ""})
    ws.append("top_bar_items", {"label": "Blog", "url": "/blog", "parent_label": "Resources"})
    ws.append("top_bar_items", {"label": "Case Studies", "url": "/case-studies", "parent_label": "Resources"})
    ws.append("top_bar_items", {"label": "About", "url": "/about", "parent_label": "Resources"})
    
    ws.append("top_bar_items", {"label": "Pricing", "url": "/pricing"})
    ws.append("top_bar_items", {"label": "Contact", "url": "/contact"})
    ws.save()

    # Services Page
    page = frappe.get_doc("Web Page", "services")
    for block in page.page_blocks:
        if block.web_template == "Section with Cards":
            vals = json.loads(block.web_template_values or "{}")
            if "title" in vals and "Service Bundles" in vals["title"]:
                new_vals = {
                    "title": vals.get("title"),
                    "subtitle": vals.get("subtitle"),
                    "card_size": "Medium",
                    "card_1_title": "Growth Operations Suite | $1,700",
                    "card_1_content": "Includes:\n\nERPNext Growth + Workflow Bundle.\n\nSavings:\n\n$300 versus separate purchase.",
                    "card_2_title": "Control & Scale Suite | $2,000",
                    "card_2_content": "Includes:\n\nERPNext Growth + Workflow Bundle + ARC Professional.\n\nSavings:\n\n$600 versus separate purchase.",
                    "card_3_title": "Enterprise Transformation Suite | $5,000+",
                    "card_3_content": "Includes:\n\nERPNext Enterprise + AI Automation Suite + ARC Enterprise.\n\nDesigned for multi-site operations and complex controls."
                }
                block.web_template_values = json.dumps(new_vals)
    page.save()

    # Home Page Pricing
    home = frappe.get_doc("Web Page", "home")
    for block in home.page_blocks:
        if block.web_template == "Section with Tabs":
            vals = json.loads(block.web_template_values or "{}")
            if "title" in vals and "Pricing Preview" in vals["title"]:
                vals["tab_1_title"] = "Starter | $500 - $1,000"
                vals["tab_1_content"] = "For small customizations & integrations.\n\nSingle module setup (Sales, Inventory, or Accounting).\n\nOne custom script or integration.\n\nData import.\n\nBasic training (1 session).\n\nEmail support for 1 month.\n\nPerfect for: New ERPNext setups, quick fixes."
                vals["tab_2_title"] = "Growth | $1,500 - $3,500"
                vals["tab_2_content"] = "Multi-module setup (Sales, Inventory, Accounting, Manufacturing).\n\nCustom workflows & automations (n8n).\n\nPayment integration.\n\nData migration & cleanup.\n\nFull team training (5 sessions).\n\n30 days of priority support.\n\nPerfect for: Growing SMEs, full system overhaul."
                vals["tab_3_title"] = "Enterprise | Custom"
                vals["tab_3_content"] = "Unlimited modules & customizations.\n\nAdvanced AI workflows & integrations.\n\nARC compliance module.\n\nCustom reporting & dashboards.\n\nDedicated support & optimization.\n\nPerfect for: Manufacturing chains, retail networks, corporates."
                block.web_template_values = json.dumps(vals)
    home.save()
    
    frappe.db.commit()
    print("Done")

