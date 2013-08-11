# -*- coding: utf-8 -*-

import unittest

from framework import TestCase

from earth.tag import Tag

class TestTagCase(TestCase):

    def test_tag(self):

        # ADD
        tag_name = '娱乐'
        tag = Tag.add(name=tag_name)
        assert tag_name == tag.name
        assert hasattr(tag, 'id')

        # GET
        tag_get = Tag.get(tag.id)
        tag_by_name = Tag.get_by_name(tag_name)
        assert tag_get == tag
        assert tag_by_name == tag

        # UPDATE
        new_tag_name = '不娱乐'
        tag.name = new_tag_name
        assert Tag.get_by_name(tag_name)
        tag.update()
        assert not Tag.get_by_name(tag_name)
        assert Tag.get_by_name(new_tag_name)

        # DELETE
        tag.delete()
        assert Tag.get(tag.id) == None
        assert Tag.get_by_name(new_tag_name) == None

    def test_tag_gets(self):

        name_cry = '哭死了'
        tag_cry = Tag.add(name=name_cry)
        assert not Tag.add(name=name_cry)

        name_laugh = '笑死了'
        tag_laugh = Tag.add(name=name_laugh)
        tags = Tag.gets([tag_cry.id, tag_laugh.id])
        assert [tag_cry, tag_laugh] == tags

if __name__ == '__main__':
    unittest.main()
