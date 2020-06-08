# -*- coding: utf-8 -*-

from .base import *  # noqa
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ['127.0.0.1']

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) # noqa

STATIC_ROOT = None

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE = ['tools.middleware.DisableCsrfCheck', 'debug_toolbar.middleware.DebugToolbarMiddleware',] \
                     + MIDDLEWARE

TEMPLATES[0]['OPTIONS'].update({'cache_size': 0})
