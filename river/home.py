# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__)

@home.route('/')
def defalut():
    try:
        return render_template('home/default.html')
    except TemplateNotFound:
        abort(404)
