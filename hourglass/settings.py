"""
Django settings for hourglass project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url

from docker_django_management import IS_RUNNING_IN_DOCKER


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

API_HOST = os.environ.get('API_HOST', '/api/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'hourglass/templates'),
    os.path.join(BASE_DIR, 'hourglass_site/templates'),
)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',

    'hourglass_site',

    'contracts',
    'api',
    'djorm_pgfulltext',
    'rest_framework',
    'corsheaders',
    'djangosecure',
)

AUTHENTICATION_BACKENDS = (
    'hourglass.uaa_backend.UAAOpenId',
)

# This is the default LOGIN_URL
# LOGIN_URL = '/accounts/login'

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'hourglass.context_processors.api_host',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

)

ROOT_URLCONF = 'hourglass.urls'

WSGI_APPLICATION = 'hourglass.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django cors headers
CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

PAGINATION = 200
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'WHITELIST': eval(os.environ.get('WHITELISTED_IPS', 'False')),
    'DEFAULT_PERMISSION_CLASSES': (
        'api.permissions.WhiteListPermission',
    ),

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
                "[%(asctime)s] %(levelname)s "
                "[%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/hourglass.log'),
            'formatter': 'verbose'
        },
        'contracts_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/load_data.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
        'contracts': {
            'handlers': ['console', 'contracts_file'],
            'propagate': True,
            'level': 'INFO',
        },
    },
}

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECURE_SSL_REDIRECT = True
# Amazon ELBs pass on X-Forwarded-Proto.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if IS_RUNNING_IN_DOCKER:
    from hourglass.docker_settings import *
else:
    try:
        from hourglass.local_settings import *
    except ImportError:
        pass

# uaa auth endpoint
# UAA_OAUTH_AUTH_URL = 'https://uaa.cloud.gov/oauth/authorize'
# UAA_OAUTH_TOKEN_URL = 'https://uaa.cloud.gov/oauth/token'

# List of required configuration variables
required_config_vars = [
    'SECRET_KEY',
    'CALC_ADMIN_EMAIL',
    'UAA_OAUTH_CALLBACK_URL',   # http(s)://<host_address>/oauth/callback
    'SOCIAL_AUTH_UAA_KEY',      # uaa client app name
    'SOCIAL_AUTH_UAA_SECRET',   # uaa client app secret
]

# Check that each required config variable has been set,
# if not, attempt to get the value from environment variable of the same name.
# This will throw a KeyError if a value is not found.
for required_var in required_config_vars:
    if required_var not in globals():
        globals()[required_var] = os.environ[required_var]
