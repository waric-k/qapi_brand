# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'
__logo__ = '/assets/whitelabel/images/whitelabel_logo.jpg'

# Optional runtime enhancement (only when frappe actually available)
try:  # pragma: no cover
    import frappe  # noqa: F401
    if getattr(frappe, 'conf', None) and frappe.conf.get('app_logo_url'):
        __logo__ = frappe.conf.get('app_logo_url') or __logo__
except Exception:
    # During build (pip PEP 517) frappe not installed; ignore
    pass