# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from nutrition.config import TERABITHIA_NAME

from earth import gets_url_by_category
from earth.url import Url
from earth.consts import DEFAULT_CATEGORIES
from earth.category import Category
from earth.relation_url_category import UrlCategoryRelation

home = Blueprint('home', __name__)

@home.route('/')
def defalut():
    default_urls = []
    for cat, limit in DEFAULT_CATEGORIES:
        category = Category.get_by_name(cat)
        urls = gets_url_by_category(category.id, limit)
        default_urls.append((category, urls))
    try:
        return render_template('home/default.html', rec_urls=default_urls)
    except TemplateNotFound:
        abort(404)
