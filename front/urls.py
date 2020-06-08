# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import path, include, re_path

from . import views
from . import views_utils

urlpatterns = [
    path('api/', include(('front.api_urls', 'front'), namespace='api')),
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    path('teacher/', views.TeacherView.as_view(), name='teacher')
]

if settings.DEBUG:
    urlpatterns += [
        path('404/', views_utils.Custom404View.as_view()),
    ]
