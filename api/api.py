
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app,prefix="/api/v1")

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///data.db")

import cmds
import macs
import tasks
