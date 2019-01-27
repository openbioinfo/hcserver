#coding=utf-8

from flask import Flask
from views.base import base

app = Flask(__name__)

app.register_blueprint(base)




