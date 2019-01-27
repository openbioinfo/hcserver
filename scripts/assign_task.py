import os
import sys
curdir = os.path.dirname(os.path.realpath(__file__))
modir = os.path.join(curdir,"../")
sys.path.append(modir)

from api.api import cmds
from api.api import macs
from api.api import tasks

def main(pyfile,ms):

    cont = open(pyfile).read()
    macs_list =  [m["macid"] for m in macs.Macs.get()[0]]
    tasks_list = tasks.Tasks.get()
    out,flag = cmds.Cmds.post({"content":cont})

    if not flag:
        sys.exit()
    cid = out["cid"]

    if ms == "all":
        ms = macs_list

    for m in ms:
        task = {"commandid":cid,"macid":m,"status":0}
        out = tasks.Tasks.post(task)
        print out

if __name__ == "__main__":
    from docopt import docopt

    usage = """
    Usage:
        assignTask.py [options] <pyfile> 

    Options:
        -m,--macs=<id1,id2,...>        devices to execute [default: all].

    """
    args = docopt(usage)
    pyfile = args["<pyfile>"]
    ms = args["--macs"]
    main(pyfile,ms)

