# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, abort

bridge = Flask(__name__)

@bridge.route("/")
def hi():
    print 'hi'
    return "Hi, welcome to Terabithia !"
