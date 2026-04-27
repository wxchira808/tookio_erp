import frappe


TABLE_TEMPLATE = """
<section class="tookio-table-wrap">
  <div class="tookio-table-head">
    <h2>{{ title }}</h2>
    {% if subtitle %}<p>{{ subtitle }}</p>{% endif %}
  </div>
  <div class="tookio-table-shell">
    <table class="tookio-before-after-table">
      <thead>
        <tr>
          <th>Function</th>
          <th>Before</th>
          <th>After Tookio ERPNext</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ row_1_function }}</td>
          <td>{{ row_1_before }}</td>
          <td>{{ row_1_after }}</td>
        </tr>
        <tr>
          <td>{{ row_2_function }}</td>
          <td>{{ row_2_before }}</td>
          <td>{{ row_2_after }}</td>
        </tr>
        <tr>
          <td>{{ row_3_function }}</td>
          <td>{{ row_3_before }}</td>
          <td>{{ row_3_after }}</td>
        </tr>
        <tr>
          <td>{{ row_4_function }}</td>
          <td>{{ row_4_before }}</td>
          <td>{{ row_4_after }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<style>
  .tookio-table-wrap { padding: 10px 0; }
  .tookio-table-head h2 { margin: 0; font-size: 1.8rem; }
  .tookio-table-head p { margin: 10px 0 22px; opacity: .8; }
  .tookio-table-shell {
    border: 1px solid rgba(255,255,255,.18);
    border-radius: 14px;
    overflow: hidden;
    background: rgba(0,0,0,.2);
    backdrop-filter: blur(4px);
  }
  .tookio-before-after-table {
    width: 100%;
    border-collapse: collapse;
  }
  .tookio-before-after-table th,
  .tookio-before-after-table td {
    text-align: left;
    padding: 14px 16px;
    vertical-align: top;
    border-bottom: 1px solid rgba(255,255,255,.1);
  }
  .tookio-before-after-table th {
    font-size: .84rem;
    text-transform: uppercase;
    letter-spacing: .04em;
    background: rgba(255,255,255,.06);
  }
  .tookio-before-after-table tbody tr:last-child td { border-bottom: 0; }
  @media (max-width: 900px) {
    .tookio-before-after-table th,
    .tookio-before-after-table td { padding: 10px 12px; font-size: .92rem; }
  }
</style>
"""


KPI_TEMPLATE = """
<section class="tookio-kpi-wrap">
  <div class="tookio-kpi-head">
    <h2>{{ title }}</h2>
    {% if subtitle %}<p>{{ subtitle }}</p>{% endif %}
  </div>

  <div class="tookio-kpi-grid">
    <article class="tookio-kpi-card">
      <h3>{{ kpi_1_label }}</h3>
      <p>{{ kpi_1_note }}</p>
      <div class="kpi-row"><span>{{ kpi_1_before_label }}</span><div class="bar"><i style="width: {{ kpi_1_before_value }}%"></i></div></div>
      <div class="kpi-row"><span>{{ kpi_1_after_label }}</span><div class="bar bar-after"><i style="width: {{ kpi_1_after_value }}%"></i></div></div>
    </article>

    <article class="tookio-kpi-card">
      <h3>{{ kpi_2_label }}</h3>
      <p>{{ kpi_2_note }}</p>
      <div class="kpi-row"><span>{{ kpi_2_before_label }}</span><div class="bar"><i style="width: {{ kpi_2_before_value }}%"></i></div></div>
      <div class="kpi-row"><span>{{ kpi_2_after_label }}</span><div class="bar bar-after"><i style="width: {{ kpi_2_after_value }}%"></i></div></div>
    </article>

    <article class="tookio-kpi-card">
      <h3>{{ kpi_3_label }}</h3>
      <p>{{ kpi_3_note }}</p>
      <div class="kpi-row"><span>{{ kpi_3_before_label }}</span><div class="bar"><i style="width: {{ kpi_3_before_value }}%"></i></div></div>
      <div class="kpi-row"><span>{{ kpi_3_after_label }}</span><div class="bar bar-after"><i style="width: {{ kpi_3_after_value }}%"></i></div></div>
    </article>
  </div>
</section>

<style>
  .tookio-kpi-wrap { padding: 12px 0; }
  .tookio-kpi-head h2 { margin: 0; font-size: 1.8rem; }
  .tookio-kpi-head p { margin: 10px 0 24px; opacity: .82; }
  .tookio-kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
  }
  .tookio-kpi-card {
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 14px;
    padding: 14px;
    background: rgba(0,0,0,.18);
  }
  .tookio-kpi-card h3 { margin: 0 0 8px; font-size: 1.06rem; }
  .tookio-kpi-card p { margin: 0 0 14px; opacity: .85; }
  .kpi-row { margin-bottom: 12px; }
  .kpi-row span { display: block; font-size: .82rem; margin-bottom: 5px; opacity: .9; }
  .bar {
    height: 10px;
    width: 100%;
    background: rgba(255,255,255,.1);
    border-radius: 999px;
    overflow: hidden;
  }
  .bar i {
    display: block;
    height: 100%;
    background: linear-gradient(90deg, #6cc4ff, #42b883);
    border-radius: 999px;
  }
  .bar-after i {
    background: linear-gradient(90deg, #f1d37a, #f8a054);
  }
  @media (max-width: 980px) {
    .tookio-kpi-grid { grid-template-columns: 1fr; }
  }
</style>
"""


def _field(fieldname, label, fieldtype="Data", mandatory=0):
    return {
        "fieldname": fieldname,
        "label": label,
        "fieldtype": fieldtype,
        "reqd": mandatory,
    }


def _upsert_template(name, template_html, fields):
    existing_name = frappe.db.get_value("Web Template", {"name": name})
    if existing_name:
        doc = frappe.get_doc("Web Template", existing_name)
        doc.type = "Section"
        doc.standard = 0
        doc.module = "Tookio Erp"
        doc.template = template_html
        doc.set("fields", [])
        for f in fields:
            doc.append("fields", f)
        doc.save(ignore_permissions=True)
        return "updated"

    doc = frappe.get_doc(
        {
            "doctype": "Web Template",
            "name": name,
            "type": "Section",
            "standard": 0,
            "module": "Tookio Erp",
            "template": template_html,
            "fields": fields,
        }
    )
    doc.insert(ignore_permissions=True)
    return "created"


@frappe.whitelist()
def upsert_tookio_web_templates():
    table_fields = [
        _field("title", "Title"),
        _field("subtitle", "Subtitle", "Small Text"),
        _field("row_1_function", "Row 1 Function"),
        _field("row_1_before", "Row 1 Before", "Small Text"),
        _field("row_1_after", "Row 1 After", "Small Text"),
        _field("row_2_function", "Row 2 Function"),
        _field("row_2_before", "Row 2 Before", "Small Text"),
        _field("row_2_after", "Row 2 After", "Small Text"),
        _field("row_3_function", "Row 3 Function"),
        _field("row_3_before", "Row 3 Before", "Small Text"),
        _field("row_3_after", "Row 3 After", "Small Text"),
        _field("row_4_function", "Row 4 Function"),
        _field("row_4_before", "Row 4 Before", "Small Text"),
        _field("row_4_after", "Row 4 After", "Small Text"),
    ]

    kpi_fields = [
        _field("title", "Title"),
        _field("subtitle", "Subtitle", "Small Text"),
        _field("kpi_1_label", "KPI 1 Label"),
        _field("kpi_1_note", "KPI 1 Note", "Small Text"),
        _field("kpi_1_before_label", "KPI 1 Before Label"),
        _field("kpi_1_before_value", "KPI 1 Before Value", "Int"),
        _field("kpi_1_after_label", "KPI 1 After Label"),
        _field("kpi_1_after_value", "KPI 1 After Value", "Int"),
        _field("kpi_2_label", "KPI 2 Label"),
        _field("kpi_2_note", "KPI 2 Note", "Small Text"),
        _field("kpi_2_before_label", "KPI 2 Before Label"),
        _field("kpi_2_before_value", "KPI 2 Before Value", "Int"),
        _field("kpi_2_after_label", "KPI 2 After Label"),
        _field("kpi_2_after_value", "KPI 2 After Value", "Int"),
        _field("kpi_3_label", "KPI 3 Label"),
        _field("kpi_3_note", "KPI 3 Note", "Small Text"),
        _field("kpi_3_before_label", "KPI 3 Before Label"),
        _field("kpi_3_before_value", "KPI 3 Before Value", "Int"),
        _field("kpi_3_after_label", "KPI 3 After Label"),
        _field("kpi_3_after_value", "KPI 3 After Value", "Int"),
    ]

    result = {
        "Tookio Before After Table": _upsert_template(
            "Tookio Before After Table", TABLE_TEMPLATE, table_fields
        ),
        "Tookio KPI Bars": _upsert_template("Tookio KPI Bars", KPI_TEMPLATE, kpi_fields),
    }
    frappe.db.commit()
    return result