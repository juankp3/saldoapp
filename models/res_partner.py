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
    movimiento_ids = fields.One2many("sa.movimiento","partner_id")

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

    total_ingresos = fields.Float("Ingresos",compute="_compute_totales")
    total_egresos = fields.Float("Egresos",compute="_compute_totales")

    #Self es un objetos de tipo partner
    @api.depends('movimiento_ids','movimiento_ids.monto_total')
    def _compute_totales(self):
        for record in self:
            movs = record.movimiento_ids #=> movimiento_ids es una lista de movimientos [sa.movimiento(1),sa.movimiento(2)....]
            record.total_egresos = sum([mov.monto_total for mov in movs if mov.tipo=="E"])
            record.total_ingresos  = sum([mov.monto_total for mov in movs if mov.tipo=="I"])

class ResUsers(models.Model):
    _inherit = "res.users"