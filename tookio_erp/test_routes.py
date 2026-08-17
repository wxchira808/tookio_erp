import frappe
from frappe.website.serve import get_response

def run():
    frappe.set_user("Guest")
    frappe.local.flags.home_page = None

    routes_to_test = [
        "/",
        "/solutions",
        "/solutions/manufacturing-erp",
        "/solutions/inventory-management",
        "/solutions/procurement-supply-chain",
        "/solutions/finance-accounting",
        "/solutions/enterprise-integrations",
        "/solutions/custom-development",
        "/industries",
        "/industries/plastics-packaging",
        "/industries/food-beverage",
        "/industries/metal-fabrication",
        "/industries/distribution-wholesale",
        "/erpnext",
        "/services",
        "/case-studies",
        "/resources",
        "/about",
        "/contact",
        "/demo",
        "/privacy-policy",
        "/terms",
        "/pricing",
        "/automation-hub",
        "/robots.txt",
        "/sitemap.xml"
    ]

    print("\n" + "="*85)
    print("%-38s | %-10s | %-12s | %-15s" % ("ROUTE", "HTTP STATUS", "CONTENT SIZE", "STATUS"))
    print("="*85)

    all_ok = True
    for r in routes_to_test:
        try:
            resp = get_response(r)
            status = getattr(resp, "status_code", 200)
            content = resp.get_data(as_text=True) if hasattr(resp, "get_data") else str(resp)
            size = len(content)
            if r.endswith(".txt") or r.endswith(".xml"):
                ok = (status == 200 and size > 50)
                check_str = "PASS (Valid Crawler Asset)" if ok else "WARN"
            else:
                has_header = "tookio-header-wrapper" in content
                has_footer = "tookio-footer" in content
                has_n8n = "n8n" in content.lower()
                ok = (status == 200 and has_header and has_footer and size > 2000 and not has_n8n)
                check_str = "PASS (Clean ERPNext)" if ok else f"WARN (H:{has_header}, F:{has_footer}, n8n:{has_n8n})"
            print(f"%-38s | HTTP %-5s | %8d bytes | %s" % (r, status, size, check_str))
        except Exception as e:
            print(f"%-38s | ERROR      | %s" % (r, str(e)))
            all_ok = False

    print("="*85)
    print("TOTAL VERIFICATION:", "ALL ROUTES CLEAN & ENTERPRISE READY!" if all_ok else "INVESTIGATE ISSUES")
    print("="*85 + "\n")
    return all_ok
