import json
from api import api,Base,engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from tools import obj2dict
from flask_restful import Resource
from flask import request
from auth import auth

Session = sessionmaker(bind=engine)

class cmds_(Base):
    
    __tablename__ = "cmds"

    cid = Column("cmdId",Integer,primary_key=True,autoincrement=True)
    content = Column("content",String)

    def __repr__(self):
        return '<cmds %s>' % self.cid

class Cmds(Resource):

    @staticmethod
    def get(self):
        session = Session()
        outs = session.query(cmds_).all()
        outs = [ obj2dict(out) for out in outs ]
        session.close()
        return outs,200

    @staticmethod
    def post(idict=None):
        session = Session()
        if not idict:
            idict = json.loads(request.data)
        obj = cmds_(**idict)
        session.add(obj)
        session.commit()
        session.close()
        return {} , 200

class Cmd(Resource) :   

    @staticmethod
    def get(cid):
        session = Session()
        out = session.query(cmds_).filter(cmds_.cid==cid).first()
        out = obj2dict(out)
        session.close()
        return out,200

    @staticmethod
    def delete(cid):
        pass

    @staticmethod
    def put(cid):
        pass

api.add_resource(Cmds,"/cmds/")
api.add_resource(Cmd,"/cmds/<cid>/")
