from flask import Flask
import json

app = Flask("__name__")


@app.route("/commands/")
def commands():
    command_content = "print 'hello world!'"

    out = {"content":command_content}
    return json.dumps(out)


@app.route("/register/")
def register():
    return "register"


@app.route("/task/")
def task():
    return ""


@app.route("/getretrun/")
    return ""



if __name__ == "__main__":
    app.run(port=5001,debug=True)



