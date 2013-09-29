# -*- coding: utf-8 -*-

import unittest

from framework import TestCase

from nutrition.database import talk

from earth.url import Url
from earth.category import Category
from earth.relation_url_category import RelationUrlCategory

class TestRelationUrlCategoryCase(TestCase):

    def test_relation(self):

        ctg_name = '社区'
        ctg = Category.add(name=ctg_name)

        url_name = '豆瓣'
        address = 'http://www.douban.com'
        url_girl = Url.add(name=url_name, url=address)
        RelationUrlCategory.add(url_id=url_girl.id, category_id=ctg.id)

        assert not RelationUrlCategory.add(url_id=url_girl.id, category_id=ctg.id)
        assert url_girl in ctg.urls()
        assert ctg in url_girl.categories()

if __name__ == '__main__':
    unittest.main()
