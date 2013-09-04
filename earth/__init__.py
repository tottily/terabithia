# -*- coding: utf-8 -*-

from .url import Url
from .category import Category

def gets_url_by_category(cat_id, limit=5):
    category = Category.get(cat_id)
    return category.urls(limit)
