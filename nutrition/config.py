# -*- coding: utf-8 -*-

from os.path import dirname

TERABITHIA_ROOT_PATH =  dirname(dirname(__file__))

MODEL_DIR = 'earth'
VIEW_DIR = 'plant'
CONTROLLER = 'river'

TEMPLATE_PATH = '%s/%s' % (TERABITHIA_ROOT_PATH, VIEW_DIR)

DB = {}
MC = {}

TERABITHIA_DOMAIN = 'http://www.dougun.com/'
TERABITHIA_NAME = '豆棍'
TERABITHIA_GLOBALS = {
    'TERABITHIA_DOMAIN': TERABITHIA_DOMAIN,
    'TERABITHIA_NAME': TERABITHIA_NAME,
}
