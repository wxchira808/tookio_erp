import frappe

def run():
    ws = frappe.get_doc("Website Settings")
    ws.google_analytics_id = "G-GZQS35TBY1"
    ws.google_analytics_anonymize_ip = 0

    robots_file = "/home/brian/frappe-bench-16/apps/tookio_erp/tookio_erp/www/robots.txt"
    try:
        with open(robots_file, "r") as f:
            ws.robots_txt = f.read()
    except Exception:
        pass

    ws.head_html = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GZQS35TBY1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-GZQS35TBY1', {
    send_page_view: true
  });
</script>
<link rel="alternate" type="text/plain" href="/llms.txt" title="LLMs.txt documentation">
"""
    ws.save(ignore_permissions=True)
    frappe.db.commit()
    print("Website Settings updated successfully with Google tag G-GZQS35TBY1 and AI robots.txt")

