# -*- coding: utf-8 -*-

import os
from os.path import dirname

TERABITHIA_ROOT_PATH =  dirname(dirname(__file__))

TERABITHIA_DOMAIN = 'http://www.dougun.com/'
TERABITHIA_NAME = '豆棍'
TERABITHIA_GLOBALS = {
    'TERABITHIA_DOMAIN': TERABITHIA_DOMAIN,
    'TERABITHIA_NAME': TERABITHIA_NAME,
}

MODEL_DIR = 'earth'
VIEW_DIR = 'plant'
CONTROLLER = 'river'

TEMPLATE_PATH = '%s/%s' % (TERABITHIA_ROOT_PATH, VIEW_DIR)

DB_CONFIG = {
    'HOST': 'localhost',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': '',
    'DB_NAME': 'terabithia',
    'ECHO': False,
}

MC_CONFIG = {}

# 单元测试的数据库配置
if os.environ.get('TEST_MODE'):
    DB_CONFIG = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
        'DB_NAME': 'test',
        'ECHO': False,
    }
