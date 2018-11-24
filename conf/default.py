# -*- coding: utf-8 -*-
"""
Django settings for app-framework project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

"""

import os
import sys
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *  # noqa


# ==============================================================================
# 应用基本信息配置 (请按照说明修改)
# ==============================================================================
# 在蓝鲸智云开发者中心 -> 点击应用ID -> 基本信息 中获取 APP_ID 和 APP_TOKEN 的值
APP_ID = 'liupeng'
APP_TOKEN = 'b0850347-93ec-4d92-84db-7637ce6d6056'
# 蓝鲸智云开发者中心的域名，形如：http://paas.bking.com
BK_PAAS_HOST = 'https://paas-poc.o.qcloud.com'

# 请求官方 API 默认版本号，可选值为："v2" 或 ""；其中，"v2"表示规范化API，""表示未规范化API
DEFAULT_BK_API_VER = 'v2'

# 是否启用celery任务
IS_USE_CELERY = True
# 本地开发的 celery 的消息队列（RabbitMQ）信息
BROKER_URL_DEV = 'amqp://guest:guest@127.0.0.1:5672/'
# TOCHANGE 调用celery任务的文件路径, List of modules to import when celery starts.
CELERY_IMPORTS = (
    'home_application.celery_tasks',
)

# ==============================================================================
# 应用运行环境配置信息
# ==============================================================================
ENVIRONMENT = os.environ.get('BK_ENV', 'development')

# 应用基本信息从环境变量中获取，未设置环境变量(如：本地开发)时，则用用户在文件开头的填写的值
APP_ID = os.environ.get('APP_ID', APP_ID)
APP_TOKEN = os.environ.get('APP_TOKEN', APP_TOKEN)
BK_PAAS_HOST = os.environ.get('BK_PAAS_HOST', BK_PAAS_HOST)
BK_PAAS_INNER_HOST = os.environ.get('BK_PAAS_INNER_HOST', BK_PAAS_HOST)

# 应用访问路径
SITE_URL = '/'
# 运行模式， DEVELOP(开发模式)， TEST(测试模式)， PRODUCT(正式模式)
RUN_MODE = 'DEVELOP'
if ENVIRONMENT.endswith('production'):
    RUN_MODE = 'PRODUCT'
    DEBUG = False
    SITE_URL = '/o/%s/' % APP_ID
elif ENVIRONMENT.endswith('testing'):
    RUN_MODE = 'TEST'
    DEBUG = False
    SITE_URL = '/t/%s/' % APP_ID
else:
    RUN_MODE = 'DEVELOP'
    DEBUG = True


try:
    import pymysql
    pymysql.install_as_MySQLdb()
except:
    pass

# ===============================================================================
# 应用基本信息
# ===============================================================================
# 应用密钥
SECRET_KEY = 'MQtd_0cw&AiY5jT&&#w7%9sCK=HW$O_e%ch4xDd*AaP(xU0s3X'
# CSRF的COOKIE域，默认使用当前域
# CSRF_COOKIE_DOMAIN =''
CSRF_COOKIE_PATH = SITE_URL

ALLOWED_HOSTS = ['*']
# ==============================================================================
# Middleware and apps
# ==============================================================================
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'account.middlewares.LoginMiddleware',   # 登录鉴权中间件
    'common.middlewares.CheckXssMiddleware',  # Xss攻击处理中间件
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # OTHER 3rd Party App
    'app_control',
    'account',
    'home_application',
)

# ==============================================================================
# Django 项目配置
# ==============================================================================
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-CN'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# 项目路径
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT, PROJECT_MODULE_NAME = os.path.split(PROJECT_PATH)
BASE_DIR = os.path.dirname(os.path.dirname(PROJECT_PATH))
PYTHON_BIN = os.path.dirname(sys.executable)

# ===============================================================================
# 静态资源设置
# ===============================================================================
# 静态资源文件(js,css等）在应用上线更新后, 由于浏览器有缓存, 可能会造成没更新的情况.
# 所以在引用静态资源的地方，都需要加上这个版本号，如：<script src="/a.js?v=${STATIC_VERSION}"></script>；
# 如果静态资源修改了以后，上线前修改这个版本号即可
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATIC_VERSION = 0.1
# 应用本地静态资源目录
STATIC_URL = '%sstatic/' % SITE_URL

ROOT_URLCONF = 'urls'
# ==============================================================================
# Templates
# ==============================================================================
# mako template dir
MAKO_TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'templates')
MAKO_TEMPLATE_MODULE_DIR = os.path.join(BASE_DIR, 'templates_module', APP_ID)
if RUN_MODE not in ['DEVELOP']:
    MAKO_TEMPLATE_MODULE_DIR = os.path.join(PROJECT_ROOT, 'templates_module', APP_ID)
# Django TEMPLATES配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # the context to the templates
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'common.context_processors.mysetting',   # 自定义模版context，可在页面中使用STATIC_URL等变量
                'django.template.context_processors.i18n',
            ],
            'debug': DEBUG
        },
    },
]
# ==============================================================================
# session and cache
# ==============================================================================
SESSION_EXPIRE_AT_BROWSER_CLOSE = True       # 默认为false,为true时SESSION_COOKIE_AGE无效
SESSION_COOKIE_PATH = SITE_URL               # NOTE 不要改动，否则，可能会改成和其他app的一样，这样会影响登录

# ===============================================================================
# Authentication
# ===============================================================================
AUTH_USER_MODEL = 'account.BkUser'
AUTHENTICATION_BACKENDS = ('account.backends.BkBackend', 'django.contrib.auth.backends.ModelBackend')
LOGIN_URL = "%s/login/?app_id=%s" % (BK_PAAS_HOST, APP_ID)
LOGOUT_URL = '%saccount/logout/' % SITE_URL
LOGIN_REDIRECT_URL = SITE_URL
REDIRECT_FIELD_NAME = "c_url"
# 验证登录的cookie名
BK_COOKIE_NAME = 'bk_token'
# 数据库初始化 管理员列表
ADMIN_USERNAME_LIST = ['admin']

# ===============================================================================
# CELERY 配置
# ===============================================================================
if IS_USE_CELERY:
    try:
        import djcelery
        INSTALLED_APPS += (
            'djcelery',            # djcelery
        )
        djcelery.setup_loader()
        CELERY_ENABLE_UTC = False
        CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
        if "celery" in sys.argv:
            DEBUG = False
        # celery 的消息队列（RabbitMQ）信息
        BROKER_URL = os.environ.get('BK_BROKER_URL', BROKER_URL_DEV)
        if RUN_MODE == 'DEVELOP':
            from celery.signals import worker_process_init

            @worker_process_init.connect
            def configure_workers(*args, **kwargs):
                import django
                django.setup()
    except:
        pass

# ==============================================================================
# logging
# ==============================================================================
# 应用日志配置
BK_LOG_DIR = os.environ.get('BK_LOG_DIR', '/data/paas/apps/logs/')
LOGGING_DIR = os.path.join(BASE_DIR, 'logs', APP_ID)
LOG_CLASS = 'logging.handlers.RotatingFileHandler'
if RUN_MODE == 'DEVELOP':
    LOG_LEVEL = 'DEBUG'
elif RUN_MODE == 'TEST':
    LOGGING_DIR = os.path.join(BK_LOG_DIR, APP_ID)
    LOG_LEVEL = 'INFO'
elif RUN_MODE == 'PRODUCT':
    LOGGING_DIR = os.path.join(BK_LOG_DIR, APP_ID)
    LOG_LEVEL = 'ERROR'

# 自动建立日志目录
if not os.path.exists(LOGGING_DIR):
    try:
        os.makedirs(LOGGING_DIR)
    except:
        pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(pathname)s %(lineno)d %(funcName)s %(process)d %(thread)d \n \t %(message)s \n',  # noqa
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s \n'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'root': {
            'class': LOG_CLASS,
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, '%s.log' % APP_ID),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },
        'component': {
            'class': LOG_CLASS,
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, 'component.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },
        'wb_mysql': {
            'class': LOG_CLASS,
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, 'wb_mysql.log'),
            'maxBytes': 1024 * 1024 * 4,
            'backupCount': 5
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        # the root logger ,用于整个project的logger
        'root': {
            'handlers': ['root'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        # 组件调用日志
        'component': {
            'handlers': ['component'],
            'level': 'WARN',
            'propagate': True,
        },
        # other loggers...
        'django.db.backends': {
            'handlers': ['wb_mysql'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
