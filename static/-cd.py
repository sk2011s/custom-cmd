from sys import dont_write_bytecode
import os
from colorama.ansi import Fore
import logging

dont_write_bytecode = True

no_args = False
args = ["dir"]
ids = ["cd", "chdir", "changedir"]
arg_type = "arg"
description = "change the working directory"

def run(dir):
    try:
        os.chdir(dir)
    except Exception as e:
        logging.error(f"Error changing directory: {e}")
        print(Fore.RED + f"Error changing directory: {e}" + Fore.WHITE)
