from flask import Flask
import json
from flask_restful import Api
from flask_restful import Resource
from flask import request
from commands import commands

app = Flask(__name__)
api = Api(app)

#@app.route("/login/",methods=["POST"])
#def login():
#    data = json.loads(request.data)
#    region = data.get("region","unknown")
#    user = data.get("user","guest")
#    passwd = data.get("passwd","guest")
#    ip = request.remote_addr
#    token = usercheck(user,passwd)
#    msg = {}
#    if token:
#        msg = {"token":token}
#        return json.dumps(msg)
#   return json.dumps(msg)


class commands_(Resource):

    def get(self):
        command = commands.get()
        out = {"content":command}
        return out,200

    def post(self):
        data = json.loads(request.data)
        cmd = data["content"]
        commands.post(cmd)

api.add_resource(commands_,"/commands/")

if __name__ == "__main__":
    app.run(port=5001,debug=True)

