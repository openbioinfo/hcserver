#!/usr/bin/env python
import sys
import os

sdir = os.path.dirname(os.path.abspath(__file__))
sdir = os.path.join(sdir,"../../")
sys.path.append(sdir)

from hcserver import app


if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0",debug=True)

