# -*- coding: utf-8 -*-

from flask import Flask

bridge = Flask(__name__)

@bridge.route("/")
def hi():
    return "Hi, welcome to Terabithia !"
