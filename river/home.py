# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from nutrition.config import TERABITHIA_NAME
from nutrition.url import DEFAULT_URLS, URLS

home = Blueprint('home', __name__)

@home.route('/')
def defalut():
    try:
        return render_template('home/default.html', urls=URLS, default_urls=DEFAULT_URLS)
    except TemplateNotFound:
        abort(404)
