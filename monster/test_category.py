# -*- coding: utf-8 -*-

import unittest

from framework import TestCase

from earth.category import Category

class TestCategoryCase(TestCase):

    def test_category(self):

        # ADD
        ctg_name = '社区'
        ctg = Category.add(name=ctg_name)
        assert ctg.id
        assert ctg.name == ctg_name
        assert ctg.pid == None

        # UPDATE
        ctg_movie = Category.add(name='电影社区', pid=ctg.id)
        assert ctg_movie.pid == ctg.id

        new_pid = 3
        other_name = '其他社区'
        ctg_movie.pid = 3
        ctg_movie.name = other_name
        ctg_movie.update()

        ctg_get = Category.get_by_name(other_name)
        assert ctg_get.id == ctg_movie.id
        assert ctg_get.name == other_name

if __name__ == '__main__':
    unittest.main()
