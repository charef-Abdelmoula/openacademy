from datetime import timedelta
from odoo import models, fields, api, exceptions, _


class Session(models.Model):
    _name = 'first_module.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    color = fields.Integer()  # kanban
    seats = fields.Integer(string="Number of seats 15")
    instructor_id = fields.Many2one('res.partner', string="Instructor",
                                    domain=[('instructor', '=', True)])  # a session has an instructor
    # ,domain=['|', ('instructor', '=', True),('category_id.name', 'ilike', "Teacher")]
    course_id = fields.Many2one('first_module.course', ondelete='cascade', string="Course", required=True)
    ###############
    # modelA modelB (we are in model A)
    # Many2one:relation will be stored in A
    # one2Many:relation ll be stored in B
    # many2many:relation ll be sstored in other table
    ##############
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    active = fields.Boolean(default=True)
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)
    invoice_count = fields.Integer(string="count invoice", compute="_compute_invoice_count")
    invoice_ids = fields.One2many("account.move", "session_id")
    # the state of  a session
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('reset', 'Reset'),
        ('cancel', 'Cancelled'),
    ], required=True, default='draft')

    # calling this function will change the state of the record to done...
    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    def button_reset(self):
        for rec in self:
            rec.state = 'reset'

    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    def facturer(self):
        id_product_template = self.env['product.template'].search([('name', 'ilike', 'Session')]).id
        id_product_product = self.env['product.product'].search([('product_tmpl_id', '=', id_product_template)]).id

        data = {
            'session_id': self.id,
            'partner_id': self.instructor_id.id,
            'type': 'in_invoice',
            "invoice_line_ids": []
            # 'partner_shipping_id' : self.instructor_id.address,
            # 'invoice_date': self.date
        }
        line = {
            "name": "session",
            "product_id": id_product_product,
            "quantity": self.duration,
            "price_unit": 10,
            # 'price_unit': self.price_per_hour
        }
        data["invoice_line_ids"].append((0, 0, line))
        # invoice1 = self.env['account.move.line'].create(line)
        invoice2 = self.env['account.move'].create(data)
        # invoice1 = self.env['account.move.line'].create(line)

    def _compute_invoice_count(self):
        self.invoice_count = self.env['account.move'].search_count([('session_id', '=', self.id)])

    def _compute_invoice_count(self):
        self.invoice_count = self.env['account.move'].search_count([('session_id', '=', self.id)])

    def action_view_invoice(self):
        invoices = self.mapped('invoice_ids')
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        if len(invoices) > 1:
            action['domain'] = [('id', 'in', invoices.ids)]
        elif len(invoices) == 1:
            form_view = [(self.env.ref('account.view_move_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = invoices.id
        else:
            action = {'type': 'ir.actions.act_window_close'}

        context = {
            'default_type': 'out_invoice',
        }

        action['context'] = context
        return action

    # graph
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    # end_date:can be deducted through duration+start_date
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    # add a constraint on the instructor and the the attendees : an attendee can t be an instructor
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError(
                    "A session's instructor can't be an attendee")  # raise for constraints not for onchange,depends apis
