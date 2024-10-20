no_args = False
args = ["dir"]
ids = ["cd", "chdir", "changedir"]
arg_type = "args"
description = "change the working directory"

import os

def run(dir):
    try:
        os.chdir(dir)
    except Exception as e:
        print(e)