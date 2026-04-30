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

    ws.app_name = "ERP For Manufacturing and Procurement Companies Kenya | Tookio"
    ws.enable_google_indexing = 0
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


def _update_block_values(block, updates):
    vals = json.loads(block.web_template_values or "{}")
    vals.update(updates)
    block.web_template_values = json.dumps(vals)


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
            "meta_title": "ERP For Manufacturing and Procurement Companies Kenya | Tookio",
            "meta_description": "Centralized ERP for Kenyan manufacturing, procurement and supply chain companies. Integrate production, stock, purchasing, HR, payroll and finance in one system.",
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
            "meta_title": "ERP Pricing Kenya | Manufacturing ERP Implementation Costs | Tookio",
            "meta_description": "KSh pricing for ERPNext implementation, automation and compliance solutions for manufacturers and procurement-heavy businesses in Kenya.",
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
        vals["title"] = "Centralized ERP for Manufacturing and Procurement Companies in Kenya"
        vals["subtitle"] = (
            "Run production, stock, procurement, sales, assets, HR and accounting from one connected operating system.\n\n"
            "Tookio helps Kenyan and East African teams replace disconnected tools with one reliable ERP backbone.\n\n"
            "Integrate machines, payment rails, banking workflows and business apps without operational silos."
        )
        home.page_blocks[0].web_template_values = json.dumps(vals)

    if len(home.page_blocks) > 2:
        vals = json.loads(home.page_blocks[2].web_template_values or "{}")
        vals["title"] = "Built for Executive-Grade Manufacturing Operations"
        vals["subtitle"] = (
            "Deploy ERP, automation and compliance controls designed for factory leadership, supply chain execution and procurement governance."
        )
        home.page_blocks[2].web_template_values = json.dumps(vals)

    if len(home.page_blocks) > 3:
        vals = json.loads(home.page_blocks[3].web_template_values or "{}")
        vals["title"] = "Case Studies with Real Operational Metrics"
        vals["subtitle"] = "Measured impact from manufacturing and operations teams in Kenya"
        vals["testimonials"] = [
            {
                "idx": 1,
                "full_name": "Finance Lead",
                "designation": "Finerate Plastics LTD",
                "content": "We centralized production, procurement, stock and invoicing in one ERP. Reconciliation cycle time dropped by over 80%, and month-end reporting became predictable.",
                "image": "/files/african-man-7398921_1280.jpg",
            },
            {
                "idx": 2,
                "full_name": "Operations Manager",
                "designation": "Manufacturing Client",
                "content": "Before Tookio we ran blind across stock and production handoffs. Now BOM execution, purchasing and fulfillment are synchronized with live KPI visibility.",
            },
            {
                "idx": 3,
                "full_name": "Commercial Lead",
                "designation": "Distribution Team",
                "content": "Invoice automation and payment matching removed manual delays. Sales, warehouse and finance now work from one version of operational truth.",
                "image": "/files/punk paradise logo.jpeg",
            },
        ]
        home.page_blocks[3].web_template_values = json.dumps(vals)

    if len(home.page_blocks) > 5:
        vals = json.loads(home.page_blocks[5].web_template_values or "{}")
        vals["title"] = "KSh Pricing Preview"
        vals["subtitle"] = "Implementation tiers built for Kenyan SME and mid-market operators"
        vals["tab_1_title"] = "Starter | KSh 80,000 - 180,000"
        vals["tab_2_title"] = "Growth | KSh 220,000 - 520,000"
        vals["tab_3_title"] = "Enterprise | From KSh 800,000"
        home.page_blocks[5].web_template_values = json.dumps(vals)

    home.save(ignore_permissions=True)


def _enhance_case_studies():
    if not frappe.db.exists("Web Page", "case-studies"):
        return

    page = frappe.get_doc("Web Page", "case-studies")

    if len(page.page_blocks) > 1:
        _update_block_values(
            page.page_blocks[1],
            {
                "title": "Portfolio Snapshot",
                "subtitle": "Centralized ERP transformations with measurable manufacturing and finance outcomes",
                "features": [
                    {
                        "idx": 1,
                        "title": "Finerate Plastics LTD",
                        "content": "Production + procurement + stock + invoicing centralized.\n\nReconciliation cycle reduced by over 80%.\n\nOperational visibility improved across plant and finance teams.",
                    },
                    {
                        "idx": 2,
                        "title": "VoltNova Dynamic Limited",
                        "content": "94% faster invoicing cycle.\n\n95% fewer invoice errors.\n\nMonth-end close reduced from 2 weeks to 2 days.",
                    },
                    {
                        "idx": 3,
                        "title": "Multi-Channel Retail Operators",
                        "content": "95% fewer overselling incidents.\n\n87% less inventory admin effort.\n\nUnified order and payment visibility.",
                    },
                ],
            },
        )

    if len(page.page_blocks) > 3:
        _update_block_values(
            page.page_blocks[3],
            {
                "title": "Case Study 2: Finerate Plastics LTD",
                "subtitle": "Manufacturing workflow optimization with centralized ERP operations",
                "features": [
                    {
                        "idx": 1,
                        "title": "Before vs After",
                        "content": "Before:\n\nProduction tracking, procurement, inventory and invoicing were fragmented across spreadsheets and disconnected tools.\n\nAfter:\n\nA centralized ERP backbone now manages manufacturing plans, material consumption, stock movements, procurement approvals, invoicing and reconciliation in one system.\n\nImpact:\n\nReconciliation effort reduced by over 80%.\n\nInvoice and payment turnaround accelerated significantly.\n\nLeadership now has one live view of operations, cash flow and fulfillment risk.",
                    }
                ],
            },
        )

    page.save(ignore_permissions=True)


def _enhance_pricing_page_ksh():
    if not frappe.db.exists("Web Page", "pricing"):
        return

    page = frappe.get_doc("Web Page", "pricing")

    if len(page.page_blocks) > 0:
        _update_block_values(
            page.page_blocks[0],
            {
                "title": "KSh Pricing for ERP Implementation in Kenya",
                "subtitle": "Executive-grade systems delivered by a focused implementation partner.\n\nNo per-user licensing surprises.",
            },
        )

    if len(page.page_blocks) > 2:
        _update_block_values(
            page.page_blocks[2],
            {
                "title": "ERPNext Implementation Packages (KSh)",
                "tab_1_title": "Starter | KSh 80,000 - 180,000",
                "tab_1_content": "Ideal for a focused first rollout.\n\n• 1-2 modules (Sales, Inventory, Accounting)\n\n• One critical custom workflow\n\n• Data migration from Excel\n\n• Team onboarding sessions\n\n• Post-go-live support\n\n• Timeline: 2-4 weeks",
                "tab_2_title": "Growth | KSh 220,000 - 520,000",
                "tab_2_content": "For serious operational transformation.\n\n• Multi-module rollout (Manufacturing, Procurement, Stock, Finance, HR)\n\n• Approval workflows + automation\n\n• Integration setup (payments, messaging, banking)\n\n• Executive dashboarding\n\n• Priority stabilization support\n\n• Timeline: 4-8 weeks",
                "tab_3_title": "Enterprise | From KSh 800,000",
                "tab_3_content": "For multi-entity or high-complexity operations.\n\n• Full architecture and governance design\n\n• Advanced automations and compliance controls\n\n• Dedicated implementation ownership\n\n• Phased deployment and optimization roadmap\n\n• Timeline: scoped by complexity",
            },
        )

    if len(page.page_blocks) > 3:
        _update_block_values(
            page.page_blocks[3],
            {
                "title": "Automation Packages (KSh)",
                "features": [
                    {
                        "idx": 1,
                        "title": "Single Workflow | KSh 35,000 - 90,000",
                        "content": "Design + implementation for one high-impact automation.\n\n• Integration with core business tools\n\n• Testing and training\n\n• Timeline: about 1 week",
                    },
                    {
                        "idx": 2,
                        "title": "Workflow Bundle | KSh 140,000 - 300,000",
                        "content": "Up to 5 automation flows across ERP and communication tools.\n\n• Operational handover + monitoring setup\n\n• Timeline: 2-4 weeks",
                    },
                    {
                        "idx": 3,
                        "title": "AI + Automation | KSh 240,000 - 480,000",
                        "content": "Includes workflow bundle plus AI-assisted operations.\n\n• Document extraction + response support\n\n• Predictive alerts and exception routing\n\n• Timeline: 3-6 weeks",
                    },
                ],
            },
        )

    if len(page.page_blocks) > 4:
        _update_block_values(
            page.page_blocks[4],
            {
                "title": "ARC Compliance Packages (KSh)",
                "features": [
                    {
                        "idx": 1,
                        "title": "Essential | KSh 80,000",
                        "content": "Incident and audit trail setup.\n\n• Basic compliance checklists\n\n• Email support",
                    },
                    {
                        "idx": 2,
                        "title": "Professional | KSh 220,000",
                        "content": "Risk module + statutory tracking.\n\n• Custom checklists and reporting\n\n• Priority support",
                    },
                    {
                        "idx": 3,
                        "title": "Enterprise | From KSh 500,000",
                        "content": "Multi-site control architecture.\n\n• Advanced dashboards\n\n• Industry-specific compliance workflows",
                    },
                ],
            },
        )

    if len(page.page_blocks) > 5:
        _update_block_values(
            page.page_blocks[5],
            {
                "title": "Bundle Offers (KSh)",
                "cards": [
                    {
                        "idx": 1,
                        "title": "Operations Core Bundle | KSh 590,000",
                        "content": "ERP Growth + Workflow Bundle.\n\nDesigned for manufacturing and procurement operations that need quick ROI.",
                    },
                    {
                        "idx": 2,
                        "title": "Control and Scale Bundle | KSh 760,000",
                        "content": "ERP Growth + Workflow Bundle + ARC Professional.\n\nStrong fit for teams scaling with compliance pressure.",
                    },
                    {
                        "idx": 3,
                        "title": "Executive Transformation Bundle | From KSh 1,500,000",
                        "content": "Enterprise ERP + AI Automation + ARC Enterprise.\n\nBest for multi-plant or multi-entity operations.",
                    },
                ],
            },
        )

    page.save(ignore_permissions=True)


def _enhance_erpnext_positioning():
    if not frappe.db.exists("Web Page", "erpnext"):
        return

    page = frappe.get_doc("Web Page", "erpnext")

    if len(page.page_blocks) > 0:
        _update_block_values(
            page.page_blocks[0],
            {
                "title": "ERPNext for Manufacturing and Procurement Companies in Kenya",
                "subtitle": "Centralize production, assets, stock, procurement, sales, HR & payroll, and accounting in one integrated system.",
                "primary_action_label": "Request Implementation Audit",
            },
        )

    if len(page.page_blocks) > 2:
        vals = json.loads(page.page_blocks[2].web_template_values or "{}")
        vals["subtitle"] = "Complete cross-functional coverage for manufacturing-led operations"
        page.page_blocks[2].web_template_values = json.dumps(vals)

    page.save(ignore_permissions=True)


def _enhance_services_ksh_archive():
    if not frappe.db.exists("Web Page", "services"):
        return

    page = frappe.get_doc("Web Page", "services")

    for block in page.page_blocks:
        vals = json.loads(block.web_template_values or "{}")
        text = json.dumps(vals)
        if "Automation + AI Pricing (USD)" in text:
            vals["title"] = "Automation + AI Pricing (KSh)"
            vals["tab_1_title"] = "Single Workflow | KSh 35,000 - 90,000"
            vals["tab_2_title"] = "Workflow Bundle | KSh 140,000 - 300,000"
            vals["tab_3_title"] = "AI + Automation Suite | KSh 240,000 - 480,000"
            block.web_template_values = json.dumps(vals)
        if "ARC Pricing (USD)" in text:
            vals["title"] = "ARC Pricing (KSh)"
            vals["tab_1_title"] = "Essential | KSh 80,000"
            vals["tab_2_title"] = "Professional | KSh 220,000"
            vals["tab_3_title"] = "Enterprise | From KSh 500,000"
            block.web_template_values = json.dumps(vals)
        if "Service Bundles (USD)" in text:
            vals["title"] = "Service Bundles (KSh)"
            vals["card_1_title"] = "Growth Operations Suite | KSh 590,000"
            vals["card_2_title"] = "Control & Scale Suite | KSh 760,000"
            vals["card_3_title"] = "Enterprise Transformation Suite | From KSh 1,500,000"
            vals["card_1_content"] = "Includes ERP Growth + Workflow Bundle.\n\nBuilt for fast-moving operations teams."
            vals["card_2_content"] = "Includes ERP Growth + Workflow Bundle + ARC Professional.\n\nAdds stronger control and compliance readiness."
            vals["card_3_content"] = "Includes Enterprise ERP + AI Automation + ARC Enterprise.\n\nDesigned for large and complex operations."
            block.web_template_values = json.dumps(vals)

    page.save(ignore_permissions=True)


def _enhance_for_enterprises_and_about():
    if frappe.db.exists("Web Page", "for-enterprises"):
        page = frappe.get_doc("Web Page", "for-enterprises")
        page.meta_title = "Enterprise ERP Rollouts Kenya | Manufacturing and Multi-Site Operations | Tookio"
        page.meta_description = "Phased ERP rollout strategy for large manufacturing and supply chain organizations in Kenya and East Africa."
        page.meta_image = "/files/erpnext-logo.png"
        if len(page.page_blocks) > 0:
            _update_block_values(
                page.page_blocks[0],
                {
                    "title": "Enterprise ERP Rollouts for Manufacturing and Multi-Site Operations",
                    "subtitle": "Governed delivery for organizations managing complex procurement, production and compliance workflows.",
                },
            )
        page.save(ignore_permissions=True)

    if frappe.db.exists("Web Page", "about"):
        page = frappe.get_doc("Web Page", "about")
        if len(page.page_blocks) > 0:
            _update_block_values(
                page.page_blocks[0],
                {
                    "title": "Built to Centralize How African Businesses Operate",
                    "subtitle": "Tookio helps leaders run manufacturing, procurement and finance with one reliable operating system.",
                },
            )
        page.save(ignore_permissions=True)


def _delete_conflicting_custom_pages():
    for page_name in ("blog", "contact"):
        if frappe.db.exists("Web Page", page_name):
            frappe.delete_doc("Web Page", page_name, force=1, ignore_permissions=True)


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
    _export_page_to_tracked_path("for-enterprises", "tookio_erp/tookio_erp/web_page/for-enterprises/for-enterprises.json")


def apply_all():
    original_enqueue = frappe.enqueue
    frappe.enqueue = lambda *args, **kwargs: None
    try:
        _set_nav()
        _create_or_update_erpnext_page()
        _unpublish_services_and_set_seo()
        _set_seo()
        _set_homepage_industry_copy()
        _enhance_case_studies()
        _enhance_pricing_page_ksh()
        _enhance_erpnext_positioning()
        _enhance_services_ksh_archive()
        _enhance_for_enterprises_and_about()
        _delete_conflicting_custom_pages()
        frappe.db.commit()
        _export_tracked_files()
        print("Applied nav, pages, SEO, pricing, and content enhancements")
    finally:
        frappe.enqueue = original_enqueue

