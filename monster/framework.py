# -*- coding: utf-8 -*-

import os
import sys
import unittest

from os.path import dirname, realpath

reload(sys)
sys.setdefaultencoding('utf8')

os.environ['TEST_MODE'] = '1'

root_path = dirname(dirname(realpath(__file__)))
sys.path.append(root_path)

from nutrition.database import establish_database, destroy_database

class TestCase(unittest.TestCase):

    def setUp(self):
        establish_database()

    def tearDown(self):
        destroy_database()

    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()




