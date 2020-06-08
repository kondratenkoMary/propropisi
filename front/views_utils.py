# -*- coding: utf-8 -*-

from django.views.generic import TemplateView

from .views import BaseView


class Custom404View(BaseView):
    template_name = 'front/pages/NotFound/NotFound.jinja'

    def get(self, request, *args, **kwargs):
        response = super(Custom404View, self).get(request, *args, **kwargs)
        response.reason_phrase = 'NOT FOUND'
        response.status_code = 404

        return response

    def get_context_data(self, **kwargs):
        context = super(Custom404View, self).get_context_data(**kwargs)

        context['page'] = '404'

        return context


class LoginView(TemplateView):
    template_name = 'front/pages/Login/Login.jinja'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        return context
