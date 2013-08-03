# -*- coding: utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__, 'plant/admin')

@admin.route('/')
def defalut():
    return 'Admin home'
