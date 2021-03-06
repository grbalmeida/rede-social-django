"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0*rgw9*#h398#i^k2xt52d+1gir7%8%c6lxxzp)fb$7#vy4w-i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    'images.apps.ImagesConfig',
    'easy_thumbnails',
    'actions.apps.ActionsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# As mensagens são armazenadas em um cookie, por padrão (recorrendo à
# armazenagem na sessão como alternativa), e serão exibidas na próxima
# requisição do usuário

# Novas mensagens podem ser criadas com o método add_message() ou com qualquer
# um dos seguintes métodos de atalho:

# success(): mensagens de sucesso a serem exibidas depois de uma ação bem-sucedida
# info(): mensagens informativas
# warning(): ainda não houve uma falha, mas poderá haver uma de forma iminente
# error(): uma ação não foi bem-sucedida ou houve uma falha
# debug(): mensagens de depuração que serão removidas ou ignoradas em um ambiente de produção

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'RedeSocialDjango',
        'USER': 'postgres',
        'PASSWORD': 'default_123'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# LOGIN_REDIRECT_URL: informa o Django o URL para o qual o usuário deverá ser
# redirecionado depois de um login bem-sucedido caso o parâmetro next não
# esteja presente na requisição
LOGIN_REDIRECT_URL = 'dashboard'
# LOGIN_URL: o URL ao qual o usuário será redirecionado para fazer login
# (por exemplo, no caso das views que utilizem o decorator login_required)
LOGIN_URL = 'login'
# LOGOUT_URL: o URL para o qual o usuário será redirecionado para fazer logout
LOGOUT_URL = 'logout'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Para permitir que Django sirva os arquivos de mídia carregados pelos usuários
# com o servidor de desenvolvimento

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# MEDIA_URL é o URL base usado para servir os arquivos de mídia cujo upload foi feito
# pelos usuários, e MEDIA_ROOT é o path local no qual estão esses arquivos.

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

# A ordem dos backends listados no parâmetro AUTHENTICATION_BACKENDS é relevante.
# Se as mesmas credenciais forem válidas para vários backends, Django encerrará
# a consulta no primeiro backend que autenticar o usuário de forma bem-sucedida

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY') # ID do App no Facebook
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET') # Código secreto do App no Facebook
# Opcionalmente, você pode definir um parâmetro SOCIAL_AUTH_FACEBOOK_SCOPE com as permissões
# extras que você queira solicitar aos usuários do Facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY') # Chave de API no Twitter
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET') # Código secreto da API no Twitter

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY') # Chave do cliente Google
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET') # Código secreto do cliente Google

from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}

# Django adiciona um método get_absolute_url() dinamicamente em qualquer
# modelo que esteja no parâmetro ABSOLUTE_URL_OVERRIDES. Esse método devolve o URL
# correspondente para o modelo especificado no parâmetro. Devolveremos o URL
# user_detail para o usuário especificado.

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0