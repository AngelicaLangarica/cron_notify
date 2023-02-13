# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from datetime import datetime

class CronNotify(models.Model):
    _name = 'cron.notify'
    _description = 'Cron Notify'

    name = fields.Char(string="Aviso", required=True)
    email_template = fields.Many2one('mail.template', string="Plantilla de correo", required=True)
    model_name = fields.Many2one('ir.model', string="Modelo", required=True, ondelete='cascade', related="email_template.model_id")
    start_date = fields.Datetime(string="Fecha de inicio", default=datetime.today(), required=True)
    interval_number = fields.Integer(string="Ejecutar cada", required=True)
    interval_type = fields.Selection([('minutes','Minutos'),('hours','Horas'),('days','Días'),('weeks','Semanas'),('months','Meses')], default="days", string="", required=True)
    cron_id = fields.Many2one('ir.cron', string="Cron", readonly=True)
    users = fields.Many2many('res.partner', string="Usuarios a notificar", required=True)