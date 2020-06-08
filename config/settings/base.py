# -*- coding: utf-8 -*-


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

config = dict()

if os.path.isfile(os.path.join(BASE_DIR, 'config.json')):
    with open(os.path.join(BASE_DIR, 'config.json')) as f:
        config = json.loads(f.read())
else:
    with open(os.path.join(BASE_DIR, 'config.test.json')) as f:
        config = json.loads(f.read())


def get_config(setting, config=config, quite=False):
    """Get the secret variable or return explicit exception."""
    try:
        return config[setting]
    except KeyError:
        if not quite:
            print("Set the {0} config parameter in config.json".format(setting))
        return None

# https://djecrety.ir/
SECRET_KEY = 'nxiym5gml745ycp#2@2gz37cpwifezh3!44t7(r7!0^ubmr_jj'

DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'front',
    'django_js_reverse',

    'rest_framework',
    'django_filters',
    'webpack_loader',
    'imagefield'
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'login_required.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(os.path.abspath(BASE_DIR), 'templates'),
                 os.path.join(os.path.abspath(BASE_DIR), 'assets', 'app'),
                 os.path.join(os.path.abspath(BASE_DIR), 'static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'auto_reload': True,
            'trim_blocks': True,
            'lstrip_blocks': True,
            'environment': 'config.jinja.environment',
            'extensions': ['jinja2.ext.do', 'jinja2.ext.loopcontrols', 'jinja2.ext.i18n', 'jinja2.ext.with_', ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_config('DB_NAME'),
        'USER': get_config('DB_USER'),
        'PASSWORD': get_config('DB_PASSWORD'),
        'HOST': get_config('DB_HOST'),
        'PORT': get_config('DB_PORT'),
        'OPTIONS': {
            'init_command': 'SET group_concat_max_len = 16384',
            'charset': 'utf8mb4'
        }
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%s:%s' % (get_config('CACHE_HOST', quite=True) or '127.0.0.1',
                               get_config('CACHE_PORT', quite=True) or '11211',),
        'KEY_PREFIX': '%s:' % (get_config('CACHE_PREFIX'),),
    },
    'cache_machine': {
        'BACKEND': 'caching.backends.memcached.MemcachedCache',
        'LOCATION': [
            '%s:%s' % (get_config('CACHE_HOST', quite=True) or '127.0.0.1',
                       get_config('CACHE_PORT', quite=True) or '11211',)
        ],
        'KEY_PREFIX': '%s:cm:' % (get_config('CACHE_PREFIX'),),
    },
}

CACHE_INVALIDATE_ON_CREATE = 'whole-model'
CACHE_COUNT_TIMEOUT = 60
CACHE_EMPTY_QUERYSETS = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_LOCATION = 'media'
MEDIA_TEMP_URL = "/%s/" % (MEDIA_LOCATION,)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = get_config('STATIC_URL') or '/static/'
MEDIA_URL = get_config('MEDIA_URL') or "/%s/" % (MEDIA_LOCATION,)

FRONT_STATS = None
CONTROL_STATS = None

try:
    with open(os.path.join(BASE_DIR, 'webpack.front.stats.json')) as front_stats:
        FRONT_STATS = json.load(front_stats)
except IOError:
    print('No webpack.front.stats.json file')

try:
    with open(os.path.join(BASE_DIR, 'webpack.control.stats.json')) as control_stats:
        CONTROL_STATS = json.load(control_stats)
except IOError:
    print('No webpack.control.stats.json file')

# Information to link builded static files with Django.
# For Django to know by what name to reference
WEBPACK_BUNDLES = {
    'front': FRONT_STATS,
    'control': CONTROL_STATS,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': '',
        'LOADER_CLASS': 'app.module.ExternalWebpackLoader',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack.stats.json'),
    }
}

SILENCED_SYSTEM_CHECKS = ["auth.W004"]

SESSION_COOKIE_AGE = 3 * 60 * 60  # 3 hours

LOGIN_URL = 'login'

LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [
    'login',
    'admin',
    'admin:index',
    'admin:login'
]

LOGIN_REQUIRED_IGNORE_VIEW_PATHS = [
    r'/admin/$',
    r'/admin/login/$',
]
