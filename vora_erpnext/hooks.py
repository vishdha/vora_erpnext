# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vora_erpnext"
app_title = "Vora Erpnext"
app_publisher = "Vishal Dhayagude"
app_description = "Custom App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vishaldhayguade07@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vora_erpnext/css/vora_erpnext.css"
# app_include_js = "/assets/vora_erpnext/js/vora_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/vora_erpnext/css/vora_erpnext.css"
# web_include_js = "/assets/vora_erpnext/js/vora_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vora_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vora_erpnext.install.before_install"
# after_install = "vora_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vora_erpnext.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vora_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"vora_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"vora_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vora_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vora_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vora_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vora_erpnext.event.get_events"
# }

fixtures = [{"dt": "Custom Field", "filters":[["name", "in", ['Sales Invoice-section_break_20', 
															'Sales Invoice-delivery_note', 'Sales Invoice-supplier_ref',
															'Sales Invoice-buyers_order_no', 'Sales Invoice-despatch_document_no',
															'Sales Invoice-despatched_through', 'Sales Invoice-country',
															'Sales Invoice-delivery_note_date', 'Sales Invoice-other_references',
                                                            'Sales Invoice-terms_of_delivery', 'Sales Invoice-column_break_28',
                                                            'Sales Invoice-buyers_order_date', 'Sales Invoice-mode_terms_of_payment',
                                                            'Sales Invoice-destination', 'Sales Invoice-e_way_bill',
                                                            'Delivery Note-section_break_14', 
															'Delivery Note-supplier_ref',
															'Delivery Note-buyers_order_no', 'Delivery Note-despatch_document_no',
															'Delivery Note-despatched_through', 'Delivery Note-country',
															'Delivery Note-other_references',
                                                            'Delivery Note-terms_of_delivery', 'Delivery Note-column_break_22',
                                                            'Delivery Note-buyers_order_date', 'Delivery Note-mode_terms_of_payment'
                                                            'Delivery Note-destination', 'Delivery Note-e_way_bill_no']]]},
            {"dt": "Print Format", "filters": [["name", "in", ["challan_cum_tax_invoice"]]]},
            {"dt": "Letter Head", "filters": [["name", "in", ["vora industries"]]]},
            {"dt": "Terms and Conditions", "filters": [["name", "in", ["Challan Cum Sales Invoice", "Delivery_note"]]]},]
