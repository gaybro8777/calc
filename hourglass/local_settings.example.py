DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hourglass',
        'USER': '',
        'PASSWORD': '',
    }
}

SECURE_SSL_REDIRECT = False

SECRET_KEY = 'I am an insecure secret key intended ONLY for dev/testing.'

CALC_ADMIN_EMAIL = ''

UAA_OAUTH_CALLBACK_URL = ''
SOCIAL_AUTH_UAA_KEY = ''
SOCIAL_AUTH_UAA_SECRET = ''
