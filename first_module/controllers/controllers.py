# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.http import request


class Academy(http.Controller):
    @http.route(['/my', '/my/home/'], auth='public', website=True)
    def index(self, **kw):
        # return "Hello, world"
        us_id = http.request.env.context.get('uid')
        Teachers = http.request.env['res.partner']
        # var=http.request.env['res.partner']
        var = http.request.env.user.partner_id.id
        return http.request.render('first_module.index', {
            'teachers': Teachers.search([]),
            'param': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
            'var': var,
            'us_id': us_id

            # http.request.env.context.get('uid') current user ('instructor_id', '!=', 57)
        })

    @http.route('/academy/<model("res.partner"):partner>/', auth='public', website=True)
    def partner(self, partner):
        return http.request.render('first_module.biography', {
            'person': partner

        })

    @http.route('/gg/<model("first_module.session"):session>/', auth='public', website=True)
    def session(self, session):
        return http.request.render('first_module.sessions', {
            'sessions': session

        })

    @http.route('/modify_session/<model("first_module.session"):session>/', auth='public',
                website=True)  # type='http',methods=['POST'],
    def modify_session(self, session):
        return http.request.render('first_module.modify_session', {
            'sessions': session

        })

    @http.route('/modify_session/session', auth='public', website=True, method=['GET'])  # type='http',methods=['POST'],
    def modify_session(self, **kwargs):
        id_sess = kwargs["id_sess"]
        # session_name=kwargs["name"]
        # session_duration
        # print(session_name)
        #
        # print("get")
        print(id_sess)
        print(kwargs["session_name"])

        session = http.request.env['first_module.session'].search([("id", "=", id_sess)])
        session.name = kwargs["session_name"]
        session.duration = kwargs["session_duration"]
        # session.session_taken_seats=kwargs["session_takent_seats"]
        # session.create(kwargs)
        # {"id": id_sess, "name": session_name}
        s = http.request.env['first_module.session'].search([("id", "=", id_sess)])
        print(s.name)

    # interface:create session
    @http.route('/create_sess', auth='public', website=True)
    def return_page(self):
        return http.request.render('first_module.create_session')
    # create a new session
    # @http.route('/create_session',auth='public',website=True,method=['POST'])
    # def create_session(self,**kw):

    # if not request.env.user._is_admin() or \
    #
    #        company.sale_quotation_onboarding_state == 'closed':

    #####################form###################

    # by name
    # @http.route('/academy/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # by id :integer
    # @http.route('/academy/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    # converter :model:provide directly the record
    # @http.route('/academy/<model("first_module.teacher"):teacher>/', auth='public', website=True)
    # def teacher(self, teacher):
    #     return http.request.render('first_module.biography', {
    #         'person': teacher
    #     })
# class FirstModule(http.Controller):
#     @http.route('/first_module/first_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
#         return "Hello, world"

#     @http.route('/first_module/first_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_module.listing', {
#             'root': '/first_module/first_module',
#             'objects': http.request.env['first_module.first_module'].search([]),
#         })

#     @http.route('/first_module/first_module/objects/<model("first_module.first_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_module.object', {
#             'object': obj
#         })
