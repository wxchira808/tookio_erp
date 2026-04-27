import frappe
import os

def extract():
    base = "/home/brian/frappe-bench-16/apps/tookio_erp/tookio_erp/tookio_erp/web_template"
    for name in ["Tookio Before After Table", "Tookio KPI Bars"]:
        doc = frappe.get_doc("Web Template", name)
        folder = os.path.join(base, frappe.scrub(name))
        os.makedirs(folder, exist_ok=True)
        html_path = os.path.join(folder, frappe.scrub(name) + ".html")
        with open(html_path, "w") as f:
            f.write(doc.template)
        print(f"Saved {html_path}")
