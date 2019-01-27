import os
import sys
curdir = os.path.dirname(os.path.realpath(__file__))
modir = os.path.join(curdir,"../")
sys.path.append(modir)

from api.cmds import Cmds

def main():
    pass


if __name__ == "__main__":
    from docopt import docopt

    usage = """
    Usage:
        assignTask.py [options] <pyfile> 

    Options:
        -m,--macs=<id1,id2,...>        devices to execute [default: all].

    """
    args = docopt(usage)
    print args

