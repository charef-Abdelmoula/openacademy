from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'first_module.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_session(self):
        return self.env['first_module.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('first_module.session',string="Session", required=True,default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def _default_sessions(self):
        return self.env['first_module.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('first_module.session',
                                   string="Sessions", required=True, default=_default_sessions)

    def subscribe(self):
        # self.session_id.attendee_ids |= self.attendee_ids
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}