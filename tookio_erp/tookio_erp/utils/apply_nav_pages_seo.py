import frappe
import json


def _set_nav():
    ws = frappe.get_doc("Website Settings", "Website Settings")
    ws.top_bar_items = []

    ws.append("top_bar_items", {"label": "ERPNext", "url": "/erpnext"})
    ws.append("top_bar_items", {"label": "ARC System", "url": "/arc-system"})
    ws.append("top_bar_items", {"label": "Automation & AI", "url": "/automation-hub"})

    ws.append("top_bar_items", {"label": "Resources", "url": ""})
    ws.append("top_bar_items", {"label": "Blog", "url": "/blog", "parent_label": "Resources"})
    ws.append("top_bar_items", {"label": "Case Studies", "url": "/case-studies", "parent_label": "Resources"})
    ws.append("top_bar_items", {"label": "About", "url": "/about", "parent_label": "Resources"})

    ws.append("top_bar_items", {"label": "Pricing", "url": "/pricing"})
    ws.append("top_bar_items", {"label": "Contact", "url": "/contact"})

    ws.google_analytics_id = "G-VHFDQR8QGN"
    ws.head_html = (
        "<script async src=\"https://www.googletagmanager.com/gtag/js?id=GT-5MJL2S8T\"></script>\n"
        "<script>\n"
        "window.dataLayer = window.dataLayer || [];\n"
        "function gtag(){dataLayer.push(arguments);}\n"
        "gtag('js', new Date());\n"
        "gtag('config', 'GT-5MJL2S8T');\n"
        "gtag('config', 'G-VHFDQR8QGN');\n"
        "</script>\n"
        "<script type=\"application/ld+json\">"
        "{"
        "\"@context\":\"https://schema.org\","
        "\"@type\":\"Organization\","
        "\"name\":\"Tookio\","
        "\"url\":\"https://tookio.co.ke\","
        "\"logo\":\"https://tookio.co.ke/files/erpnext-logo.png\","
        "\"description\":\"ERP implementation, automation and ARC compliance solutions for manufacturing, procurement and supply chain teams in Kenya and East Africa.\""
        "}"
        "</script>\n"
        "<script type=\"application/ld+json\">"
        "{"
        "\"@context\":\"https://schema.org\","
        "\"@type\":\"WebSite\","
        "\"name\":\"Tookio\","
        "\"url\":\"https://tookio.co.ke\","
        "\"potentialAction\":{"
        "\"@type\":\"SearchAction\","
        "\"target\":\"https://tookio.co.ke/search?q={search_term_string}\","
        "\"query-input\":\"required name=search_term_string\""
        "}"
        "}"
        "</script>"
    )
    ws.save()


def _create_or_update_erpnext_page():
    services = frappe.get_doc("Web Page", "services")

    # ERPNext-focused section blocks from services page
    erp_blocks = []
    for i, block in enumerate(services.page_blocks):
        if i in (1, 2, 3, 4, 5, 6):
            erp_blocks.append(block.as_dict())

    if frappe.db.exists("Web Page", "erpnext"):
        erp = frappe.get_doc("Web Page", "erpnext")
    else:
        erp = frappe.new_doc("Web Page")
        erp.name = "erpnext"

    erp.title = "ERPNext"
    erp.route = "erpnext"
    erp.module = "Tookio Erp"
    erp.content_type = "Page Builder"
    erp.full_width = 1
    erp.show_title = 0
    erp.show_sidebar = 0
    erp.dynamic_route = 0
    erp.dynamic_template = 0
    erp.enable_comments = 0
    erp.text_align = "Left"
    erp.published = 1

    erp.meta_title = "ERPNext Implementation in Kenya | Manufacturing, Procurement & Supply Chain | Tookio"
    erp.meta_description = (
        "Tookio delivers ERPNext implementation in Kenya and East Africa for manufacturing, "
        "procurement and supply chain operations with integrations to machines and third-party systems."
    )
    erp.meta_image = "/files/erpnext-logo.png"

    erp.page_blocks = []
    for b in erp_blocks:
        for k in ("name", "owner", "creation", "modified", "modified_by", "docstatus", "doctype", "parent", "parentfield", "parenttype", "idx"):
            b.pop(k, None)
        erp.append("page_blocks", b)

    if erp.is_new():
        erp.insert(ignore_permissions=True)
    else:
        erp.save(ignore_permissions=True)


def _unpublish_services_and_set_seo():
    services = frappe.get_doc("Web Page", "services")
    services.published = 0
    services.meta_title = "Business Systems Solutions | ERPNext, Automation and ARC | Tookio"
    services.meta_description = (
        "Integrated systems by Tookio: ERPNext, automation and ARC compliance solutions for East African businesses."
    )
    services.meta_image = "/files/erpnext-logo.png"
    services.save(ignore_permissions=True)


def _set_seo():
    seo = {
        "home": {
            "meta_title": "ERP for Manufacturing in Kenya | Procurement & Supply Chain Systems | Tookio",
            "meta_description": "Kenyan ERP implementation partner for manufacturing, procurement and supply chain companies. Integrate finance, inventory, production and machine-linked workflows.",
            "meta_image": "/files/erpnext-logo.png",
        },
        "arc-system": {
            "meta_title": "Audit Risk and Compliance System Kenya | ARC by Tookio",
            "meta_description": "ARC compliance software for Kenyan and East African businesses. Centralize audit trails, risk registers and regulatory controls.",
            "meta_image": "/files/shield-checkmark.png",
        },
        "automation-hub": {
            "meta_title": "Automation & AI for ERP in Kenya | Tookio",
            "meta_description": "Automate procurement, finance and supply chain workflows with n8n and AI integrations across ERPNext and third-party systems.",
            "meta_image": "/files/n8n icon.png",
        },
        "pricing": {
            "meta_title": "ERP, Automation and Compliance Pricing Kenya | Tookio",
            "meta_description": "Transparent pricing for ERPNext implementation, automation and ARC compliance solutions in Kenya and East Africa.",
            "meta_image": "/files/erpnext-logo.png",
        },
        "case-studies": {
            "meta_title": "ERP Manufacturing Case Studies Kenya | Tookio",
            "meta_description": "Case studies showing ERPNext, procurement and supply chain transformation outcomes for Kenyan and East African businesses.",
            "meta_image": "/files/erpnext-logo.png",
        },
        "about": {
            "meta_title": "About Tookio | ERP and Manufacturing Systems Partner in Kenya",
            "meta_description": "Tookio helps manufacturing, procurement and supply chain businesses in Kenya and East Africa deploy practical ERP, automation and compliance systems.",
            "meta_image": "/files/erpnext-logo.png",
        },
        "blog": {
            "meta_title": "ERP and Supply Chain Insights Kenya | Tookio Blog",
            "meta_description": "Insights on ERPNext, manufacturing operations, procurement workflows and supply chain digitization in Kenya and East Africa.",
            "meta_image": "/files/erpnext-logo.png",
        },
        "contact": {
            "meta_title": "Contact Tookio | ERPNext for Manufacturing and Supply Chain in Kenya",
            "meta_description": "Talk to Tookio about ERP implementation, procurement process automation and supply chain integration for Kenyan operations.",
            "meta_image": "/files/erpnext-logo.png",
        },
    }

    for page_name, vals in seo.items():
        if frappe.db.exists("Web Page", page_name):
            page = frappe.get_doc("Web Page", page_name)
            page.meta_title = vals["meta_title"]
            page.meta_description = vals["meta_description"]
            page.meta_image = vals["meta_image"]
            page.save(ignore_permissions=True)


def _set_homepage_industry_copy():
    if not frappe.db.exists("Web Page", "home"):
        return

    home = frappe.get_doc("Web Page", "home")

    if len(home.page_blocks) > 0:
        vals = json.loads(home.page_blocks[0].web_template_values or "{}")
        vals["title"] = "ERP for Manufacturing, Procurement and Supply Chain in Kenya"
        vals["subtitle"] = (
            "Replace spreadsheet chaos with one integrated operating system for Kenyan and East African operations.\n\n"
            "Tookio implements ERPNext for manufacturers, distributors and procurement-heavy teams.\n\n"
            "Connect inventory, production, purchasing, finance and machine-adjacent workflows in one platform."
        )
        home.page_blocks[0].web_template_values = json.dumps(vals)

    if len(home.page_blocks) > 2:
        vals = json.loads(home.page_blocks[2].web_template_values or "{}")
        vals["title"] = "Built for Manufacturing and Procurement Teams in East Africa"
        vals["subtitle"] = (
            "Deploy ERP, automation and compliance controls designed for factory operations, supply chain teams and procurement leaders."
        )
        home.page_blocks[2].web_template_values = json.dumps(vals)

    home.save(ignore_permissions=True)


def _export_page_to_tracked_path(page_name, target_rel_path):
    doc = frappe.get_doc("Web Page", page_name)
    target_path = f"/home/brian/frappe-bench-16/apps/tookio_erp/{target_rel_path}"
    with open(target_path, "w") as f:
        f.write(frappe.as_json(doc.as_dict(no_nulls=True), indent=1))


def _export_tracked_files():
    _export_page_to_tracked_path("erpnext", "tookio_erp/tookio_erp/web_page/erpnext/erpnext.json")
    _export_page_to_tracked_path("services", "tookio_erp/tookio_erp/web_page/services/services.json")
    _export_page_to_tracked_path("home", "tookio_erp/tookio_erp/web_page/home/home.json")
    _export_page_to_tracked_path("arc-system", "tookio_erp/tookio_erp/web_page/arc-system/arc-system.json")
    _export_page_to_tracked_path("automation-hub", "tookio_erp/tookio_erp/web_page/automation-hub/automation-hub.json")
    _export_page_to_tracked_path("pricing", "tookio_erp/tookio_erp/web_page/pricing/pricing.json")
    _export_page_to_tracked_path("case-studies", "tookio_erp/tookio_erp/web_page/case-studies/case-studies.json")
    _export_page_to_tracked_path("about", "tookio_erp/tookio_erp/web_page/about/about.json")
    _export_page_to_tracked_path("blog", "tookio_erp/tookio_erp/web_page/blog/blog.json")
    _export_page_to_tracked_path("contact", "tookio_erp/tookio_erp/web_page/contact/contact.json")


def apply_all():
    _set_nav()
    _create_or_update_erpnext_page()
    _unpublish_services_and_set_seo()
    _set_seo()
    _set_homepage_industry_copy()
    frappe.db.commit()
    _export_tracked_files()
    print("Applied nav, pages, and SEO updates")

