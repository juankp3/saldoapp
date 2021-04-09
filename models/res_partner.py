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

    def action_mi_perfil (self):
        res_users_obj = self.env.user.id
        return {
            'name' : 'Mi Perfil',
            'res_model' : 'res.urers',
            'view_mode' : 'tree,form',
            'res_id' : res_users_obj.id,
            'target' : 'self'
        }