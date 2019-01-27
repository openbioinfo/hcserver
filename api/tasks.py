print "tasks exec..."
import json
from flask_restful import Resource
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker
from api import api,Base,engine
import macs
import cmds
from tools import obj2dict
from flask import request

Session = sessionmaker(bind=engine)

class tasks_(Base):
    
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}
    taskid = Column("taskId",Integer,primary_key=True,autoincrement=True)
    macid = Column("macId",Integer,ForeignKey(macs.macs_.id))
    commandid = Column("cmdId",Integer,ForeignKey(cmds.cmds_.cid))
    status = Column("status",Integer)

    def __repr__(self):
        return '<task %s>' % self.taskid

class Tasks(Resource):

    @staticmethod
    def get(filterDict={}):
        try:
            filterDict = dict(request.args.items())
        except:
            pass
        session = Session()
        ts = session.query(tasks_).filter_by(**filterDict).all()
        ts = [ obj2dict(t) for t in ts ]
        session.close()
        return ts

    @staticmethod
    def post(idict=None):
        if not idict:
            idict = json.loads(request.data)
        obj = tasks_(**idict)
        session = Session()
        session.add(obj)
        session.commit()
        odict = obj2dict(obj)
        session.close()
        return odict,200

class Task(Resource):

    @staticmethod
    def get(tid):
        session = Session()
        m = session.query(tasks_).filter(tasks_.taskid==tid).first()
        m = obj2dict(m)
        session.close()
        return m,200

    @staticmethod
    def delete():
        pass

    @staticmethod
    def put():
        pass

api.add_resource(Tasks,"/tasks/")
api.add_resource(Task,"/tasks/<tid>/")
print "tasks loaded..."
