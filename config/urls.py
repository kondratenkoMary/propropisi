"""starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.views.static import serve

from front.views_utils import Custom404View, LoginView


handler404 = None

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^', include(('front.urls', 'front'), namespace='front')),
]

if not handler404:
    handler404 = Custom404View.as_view()

if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
                            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), ]

    import debug_toolbar

    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

