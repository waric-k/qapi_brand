__version__ = "0.0.1"


def get_logo():
	try:
		import frappe

		if frappe.conf and frappe.conf.get("app_logo_url"):
			return frappe.conf.get("app_logo_url") or "/assets/whitelabel/images/whitelabel_logo.png"
		else:
			return "/assets/whitelabel/images/whitelabel_logo.png"
	except ImportError:
		return "/assets/whitelabel/images/whitelabel_logo.png"


__logo__ = get_logo()
