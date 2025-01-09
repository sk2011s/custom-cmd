from sys import dont_write_bytecode

dont_write_bytecode = True


no_args = True
args = []
ids = ["exit", "e"]
arg_type = "args"
description = "exit the program"


@staticmethod
def run():
    return -1
