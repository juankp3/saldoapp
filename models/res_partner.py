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

    def accion_mi_perfil(self):
        res_users_id = self.env.uid
        res_users_obj = self.env["res.users"].search([["id","=",res_users_id]])
        if res_users_obj:
            res_partner_id = res_users_obj.partner_id.id
        view_form_obj = self.env.ref("base.view_partner_form")
        return {
            "type":"ir.actions.act_window",
            "name":"Mi Perfil",
            "res_model":"res.partner",
            "view_id":view_form_obj.id,
            "view_mode":"form",
            "res_id":res_partner_id,
            "target":"self"
        }

class ResUsers(models.Model):
    _inherit = "res.users"