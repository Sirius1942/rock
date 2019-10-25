"""
Django settings for basepro project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from datetime import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yg@o)vx*3g4+kjqp(tj!qx2kp(3k%&va%x#j(4ot%fv3r$^#=p'

# #htts setting
# SECURE_SSL_REDIRECT = True 
# # //将所有非SSL请求永久重定向到SSL
# SECURE_HSTS_SECONDS = 2
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
# # //使用[HTTP严格传输安全]
# SECURE_FRAME_DENY = True 
# # //避免让自己的网页的框架和保护他们免受[点击劫持]
# SECURE_CONTENT_TYPE_NOSNIFF = True 
# # //防止浏览器猜测资产的内容类型
# SECURE_BROWSER_XSS_FILTER = True  
# # //启用浏览器的XSS过滤保护
# SESSION_COOKIE_SECURE = True 
# SESSION_COOKIE_HTTPONLY = True 
# # //防止COOKIE窃听，使客户端到服务端总是COOKIE加密传输

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# 添加AUTH_USRE_MODEL 替换默认的user
AUTH_USER_MODEL = 'user.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user.apps.UserConfig',
    'corsheaders',
    'emyxin.apps.EmyxinConfig',
    'werkzeug_debugger_runserver',
    'django_extensions',
]

MIDDLEWARE = [
    # 'djangosecure.middleware.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'basepro.urls'

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

WSGI_APPLICATION = 'basepro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    #使用sqllite 的配置 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db/db.sqlite3'),
    }
    # # 使用MySql的配置，注意需要先手工创建数据库,初始化未成功无法后续再修改Related model 'user.UserProfile' cannot be resolved
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'rock',
    #     'USER': 'root',
    #     'PASSWORD':'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    #     'CHARSET':'utf-8',
    #     'COLLATION':'utf-8_general_ci',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    )
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
# //跨域配置https://github.com/ottoyiu/django-cors-headers/

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST  = ('*')
#     #  “ https://example.com ”，
#     #  “ https://sub.example.com ”，
#     #  “ http：// localhost：8080 ”，
#     # "http://127.0.0.1:8888",
#     # "http://localhost:8888",
#     # "http://localhost:9527",
#     # "http://127.0.0.0:9527",
    
# CORS_ORIGIN_REGEX_WHITELIST  = [
#      - [R “ ^ HTTPS：// \ W + \例子。\ COM $ ”，
# ]

CORS_ALLOW_METHODS  = [
     ' DELETE ',
     ' GET ',
     ' OPTIONS ',
     ' PATCH ',
     ' POST ',
     ' PUT ',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')