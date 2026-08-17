app_name = "tookio_erp"
app_title = "Tookio Erp"
app_publisher = "Tookio"
app_description = "Custom app for main site"
app_email = "tookiosolutions@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tookio_erp",
# 		"logo": "/assets/tookio_erp/logo.png",
# 		"title": "Tookio Erp",
# 		"route": "/tookio_erp",
# 		"has_permission": "tookio_erp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tookio_erp/css/tookio_erp.css"
# app_include_js = "/assets/tookio_erp/js/tookio_erp.js"

# include js, css files in header of web template
web_include_css = "/assets/tookio_erp/css/tookio_enterprise.css"
web_include_js = "/assets/tookio_erp/js/tookio_enterprise.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

website_route_rules = [
	{"from_route": "/contacts", "to_route": "contact"},
	{"from_route": "/get-started", "to_route": "demo"},
	{"from_route": "/terms-of-service", "to_route": "terms"},
	{"from_route": "/home", "to_route": "index"},
	{"from_route": "/pricing", "to_route": "contact"},
	{"from_route": "/automation-hub", "to_route": "solutions/enterprise-integrations"}
]

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tookio_erp.utils.jinja_methods",
# 	"filters": "tookio_erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tookio_erp.install.before_install"
# after_install = "tookio_erp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tookio_erp.uninstall.before_uninstall"
# after_uninstall = "tookio_erp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tookio_erp.utils.before_app_install"
# after_app_install = "tookio_erp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tookio_erp.utils.before_app_uninstall"
# after_app_uninstall = "tookio_erp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tookio_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tookio_erp.tasks.all"
# 	],
# 	"daily": [
# 		"tookio_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"tookio_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tookio_erp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tookio_erp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tookio_erp.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tookio_erp.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tookio_erp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tookio_erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tookio_erp.utils.before_request"]
# after_request = ["tookio_erp.utils.after_request"]

# Job Events
# ----------
# before_job = ["tookio_erp.utils.before_job"]
# after_job = ["tookio_erp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tookio_erp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

