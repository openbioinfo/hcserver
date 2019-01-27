print "macs exec..."
import json
from flask_restful import Resource
from api import api, Base,engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from tools import obj2dict
from flask import request

Session = sessionmaker(bind=engine)

class macs_(Base):

    __tablename__ = "macs"
    __table_args__ = {'extend_existing': True} 
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    macid = Column("macid",Integer,index=True,unique=True)
    region = Column("region",String)
    owner = Column("owner",String)

    def __repr__(self):
        return "<macs %s>" % self.id

class Macs(Resource):

    @staticmethod
    def get():
        session = Session()
        ms = session.query(macs_).all()
        mlist = [obj2dict(m) for m in ms]
        session.close()
        return mlist,200

    @staticmethod
    def post(amac=None):
        if not amac:
            amac = json.loads(request.data)
        machine = macs_(**amac)
        session = Session()
        session.add(machine)
        session.commit()
        session.close()
        return {},200

class Mac(Resource):
   
    @staticmethod
    def get(mid):
        session = Session()
        m = session.query(macs_).filter(macs_.macid==mid).first()
        md = obj2dict(m)    
        session.close() 
        return md,200
   
    @staticmethod
    def delete():
        pass

    @staticmethod
    def put():
        pass


api.add_resource(Macs,"/macs/")
api.add_resource(Mac,"/macs/<mid>/")
print "macs loaded..."
