# -*- coding: utf-8 -*-
# Copyright (c) 2017, Arpit Jain and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
import frappe.defaults
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname



def naming_series(self,method):
	print "khushal##########################"