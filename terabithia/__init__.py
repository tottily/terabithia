# -*- coding: utf-8 -*-

from flask import Flask
from river import home, admin

app = Flask('Terabithia')

rivers = {
    home: '/',
    admin: '/admin',
}

for router, prefix in rivers.items():
    app.register_blueprint(router, url_prefix=prefix)

