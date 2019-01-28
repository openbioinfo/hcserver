#coding=utf-8

from flask import Flask
from views.base import base
from views.tasks import tasks

app = Flask(__name__)

app.register_blueprint(base)
app.register_blueprint(tasks)
