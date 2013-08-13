# -*- coding: utf-8 -*-

import time
import hashlib
import unittest

from framework import TestCase

from earth.url import Url

class TestUrlCase(TestCase):

    def test_url(self):
        pass

        # ADD
        url_name = '豆瓣'
        address = 'http://www.douban.com'
        url_girl = Url.add(name=url_name, url=address)
        old_refresh_time = url_girl.refresh_time
        time.sleep(1)

        assert url_girl.url == address
        assert url_girl.name == url_name
        assert url_girl.refresh_time
        assert url_girl.md5 == hashlib.md5(address).hexdigest()

        assert not Url.add(name=url_name, url=address)
        assert Url.get_by_url(address) == url_girl

        # UPDATE
        new_girl_name = '豆小瓣'
        url_girl.name = new_girl_name
        url_girl.update()
        assert url_girl.name == new_girl_name
        assert url_girl.refresh_time != old_refresh_time

        address_boy = 'http://www.dougun.com'
        url_boy = Url.add(name=url_name, url=address_boy)
        url_boy.url = address
        assert not url_boy.update()
        assert url_boy.url == address_boy

        # DELETE
        boy_id = url_boy.id
        url_boy.delete()
        assert Url.get(boy_id) == None
        assert Url.get_by_url(address_boy) == None

if __name__ == '__main__':
    unittest.main()
