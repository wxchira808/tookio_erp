import frappe
import json

def apply_custom_templates():
    page = frappe.get_doc("Web Page", "services")
    
    # Block 2 (0-indexed) -> Tookio Before After Table
    if len(page.page_blocks) > 2:
        page.page_blocks[2].web_template = "Tookio Before After Table"
        page.page_blocks[2].web_template_values = json.dumps({
            "title": "What ERPNext Looks Like in Practice",
            "subtitle": "One connected system across core business functions",
            "row_1_function": "Sales",
            "row_1_before": "Orders spread across chat and calls",
            "row_1_after": "Pipeline, quotations, and orders in one workflow",
            "row_2_function": "Inventory",
            "row_2_before": "Periodic manual counts",
            "row_2_after": "Real-time stock updates and alerts",
            "row_3_function": "Finance",
            "row_3_before": "Delayed reconciliation and close",
            "row_3_after": "Automated entries, faster close",
            "row_4_function": "HR",
            "row_4_before": "Manual leave follow-up",
            "row_4_after": "Integrated payroll visibility"
        })
    
    # Block 5 (0-indexed) -> Tookio KPI Bars
    if len(page.page_blocks) > 5:
        page.page_blocks[5].web_template = "Tookio KPI Bars"
        page.page_blocks[5].web_template_values = json.dumps({
            "title": "Performance Snapshot (Typical Outcomes)",
            "subtitle": "KPI chart view from recent implementation patterns",
            "kpi_1_label": "Invoice Cycle Time",
            "kpi_1_note": "Up to 92% faster",
            "kpi_1_before_label": "Before",
            "kpi_1_before_value": 100,
            "kpi_1_after_label": "After",
            "kpi_1_after_value": 8,
            "kpi_2_label": "Reconciliation Effort",
            "kpi_2_note": "Up to 88% reduction",
            "kpi_2_before_label": "Before",
            "kpi_2_before_value": 100,
            "kpi_2_after_label": "After",
            "kpi_2_after_value": 12,
            "kpi_3_label": "Data Accuracy Control",
            "kpi_3_note": "Significantly improved visibility",
            "kpi_3_before_label": "Before",
            "kpi_3_before_value": 40,
            "kpi_3_after_label": "After",
            "kpi_3_after_value": 90
        })
    
    page.save()
    frappe.db.commit()

apply_custom_templates()
print("Applied and saved!")
