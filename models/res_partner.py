# -*- coding: utf-8 -*-

from odoo import models, fields, api

"""
Clase models.Model
===================
Python --> SQL
create() --> Insert
write() --> update
unlink()  --> delete
search(),browse() --> select *
"""

class ResPartner(models.Model):
    _inherit = "res.partner"
    fecha_cumple = fields.Date("Fecha de Cumpleaños")