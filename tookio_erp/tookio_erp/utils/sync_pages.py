import frappe
import json
import os

def sync_page(page_name):
    json_path = f"/home/brian/frappe-bench-16/apps/tookio_erp/tookio_erp/tookio_erp/web_page/{page_name}/{page_name}.json"
    if not os.path.exists(json_path):
        return
    with open(json_path, "r") as f:
        data = json.load(f)
    
    doc = frappe.get_doc("Web Page", page_name)
    doc.page_blocks = []
    
    for block in data.get("page_blocks", []):
        # clean block internal identifiers
        for k in ["name", "owner", "modified_by", "creation", "modified", "idx", "__islocal"]:
            block.pop(k, None)
        doc.append("page_blocks", block)
        
    doc.save()
    frappe.db.commit()
    print(f"Synced {page_name}")

def sync_all():
    sync_page("services")
    sync_page("home")
    sync_page("pricing")
    sync_page("for-enterprises")

