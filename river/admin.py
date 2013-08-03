# -*- coding: utf-8 -*-

from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort

admin = Blueprint('admin', __name__)

@admin.route('/')
def defalut():
    try:
        return render_template('admin/default.html')
    except TemplateNotFound:
        abort(404)
