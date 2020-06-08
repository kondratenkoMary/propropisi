# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.utils import timezone
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

import json

from . import models
from . import data
from .serializers.student import StudentSerializer
from .serializers.teacher import TeacherSerializer


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        return context


class IndexView(BaseView):
    template_name = 'front/pages/Index/Index.jinja'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['student'] = json.loads(CamelCaseJSONRenderer().render(
            StudentSerializer(
                models.Student.objects.get(id=3)
            ).data
        ))

        context['statuses'] = data.statuses

        return context


class TeacherView(BaseView):
    template_name = 'front/pages/Teacher/Teacher.jinja'

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)

        context['taskStatuses'] = data.task_statuses
        context['teacher'] = data.teacher
        context['teacher'] = json.loads(CamelCaseJSONRenderer().render(
            TeacherSerializer(
                models.Teacher.objects.get(id=2)
            ).data
        ))

        return context
