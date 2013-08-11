# -*- coding: utf-8 -*-

import unittest
from framework import TestCase

from earth.tag import Tag

class TestTagCase(TestCase):

    def test_tag(self):
        tag_name = 'tag1'
        tag = Tag.add(name=tag_name)
        assert tag_name == tag.name

        tag_get = Tag.get(tag.id)
        assert tag_get == tag

        tag.delete()
        assert Tag.get(tag.id) == None


if __name__ == '__main__':
    unittest.main()




