# -*- coding: utf-8 -*-

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .api import common

router = DefaultRouter()
router.register(r'solution', common.SolutionViewSet, basename='solution')

urlpatterns = [
    path('', include(router.urls))
]
