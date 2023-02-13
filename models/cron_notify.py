# -*- coding: utf-8 -*-

from flectra import models, fields, api, _
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)
class CronNotify(models.Model):
    _name = 'cron.notify'
    _description = 'Cron Notify'

    name = fields.Char(string="Aviso", required=True)
    email_template = fields.Many2one('mail.template', string="Plantilla de correo", required=True, readonly=True, default=lambda self: self.env.ref('cron_notify.email_sent_notify').id)
    model_name = fields.Many2one('ir.model', string="Modelo", required=True, ondelete='cascade', related="email_template.model_id")
    start_date = fields.Datetime(string="Fecha de inicio", default=datetime.today(), required=True)
    interval_number = fields.Integer(string="Ejecutar cada", required=True)
    interval_type = fields.Selection([('minutes','Minutos'),('hours','Horas'),('days','Días'),('weeks','Semanas'),('months','Meses')], default="days", string="", required=True)
    cron_id = fields.Many2one('ir.cron', string="Cron", readonly=True)
    users = fields.Many2many('res.partner', string="Usuarios a notificar", required=True)
    company_id = fields.Many2one('res.company', string="Compañia", default=lambda self: self.env.company)

    def create_cron(self):
        data = {
            'name': self.name,
            'model_id': self.model_name.id,
            'user_id': self.env.ref('base.user_admin').id,
            'interval_number': self.interval_number,
            'interval_type': self.interval_type,
            'active': 1,
            'nextcall': self.start_date,
            'numbercall': -1,
            'code': 'model.sent_mail_notify()',
        }
        cron = self.env['ir.cron'].sudo().create(data)
        if cron:
            self.cron_id = cron.id
    
    def sent_mail_notify(self):
        for item in self.search([]):
            values = item.email_template.generate_email(item.id, ['subject', 'email_from', 'email_to','body_html'])
            for user in item.users:
                values['email_to'] = user.email or ''
                mail = self.env['mail.mail'].create(values)
                try:
                    mail.send()
                except Exception:
                    pass