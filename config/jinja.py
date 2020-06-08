# -*- coding: utf-8 -*-
import json
import os

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.template.loader import engines
from django.utils.html import linebreaks, escape

from jinja2 import Environment
from webpack_loader.templatetags import webpack_loader

from django.conf import settings


def includeraw(template):
    env = engines['jinja2'].env
    source, fn, _ = env.loader.get_source(env, template)

    return source


def jsonify(value):
    return json.dumps(value)


def require(template):
    return includeraw(template)


def nl2br(input):
    return linebreaks(escape(input))


def environment(**options):
    env = Environment(**options)

    if os.path.isfile(os.path.join(settings.BASE_DIR, 'config.json')):
        with open(os.path.join(settings.BASE_DIR, 'config.json')) as f:
            config = json.loads(f.read())
    else:
        with open(os.path.join(settings.BASE_DIR, 'config.test.json')) as f:
            config = json.loads(f.read())

    env.filters['jsonify'] = jsonify
    env.filters['require'] = require
    env.filters['nl2br'] = nl2br

    env.globals.update({
        'static': staticfiles_storage.url,
        'render_bundle': webpack_loader.render_bundle,
        'url': reverse,
        'config': config,
        'settings': settings,
        'DEBUG': settings.DEBUG,
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,
        'includeraw': includeraw
    })
    return env
