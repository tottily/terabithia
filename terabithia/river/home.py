# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from nutrition.config import TERABITHIA_ROOT_PATH

home = Blueprint('home', __name__, template_folder='%s/plant/home/' % TERABITHIA_ROOT_PATH)

@home.route('/')
def defalut():
    try:
        return render_template('default.html')
    except TemplateNotFound:
        abort(404)
