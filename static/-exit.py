from sys import dont_write_bytecode
import logging

dont_write_bytecode = True

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

no_args = True
args = []
ids = ["exit", "e"]
arg_type = "args"
description = "exit the program"

@staticmethod
def run():
    return -1
