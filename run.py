# -*- coding: utf-8 -*-

import sys

from os.path import dirname, realpath

ROOT_PATH = '%s/terabithia' % dirname(realpath(__file__))
sys.path.append(ROOT_PATH)

from terabithia import app
app.run(host='localhost', port=80, debug=True)
