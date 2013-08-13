# -*- coding: utf-8 -*-

from .url import Url
from .relation_url_category import UrlCategoryRelation

def gets_url_by_category(cat_id, limit=5):
    relations = UrlCategoryRelation.query.filter(UrlCategoryRelation.category_id == cat_id).limit(limit)
    ids = [relation.url_id for relation in relations]
    return Url.gets(ids)
