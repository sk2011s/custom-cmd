from os import system as bat
from colorama.ansi import Fore
from sys import dont_write_bytecode
import logging

dont_write_bytecode = True

no_args = False
args = ["command"]
ids = ["cmd"]
arg_type = "arg"
description = "run cmd command"

@staticmethod
def run(*args):
    try:
        command = " ".join(args)
        bat(command)
    except Exception as e:
        logging.error(f"Error: {e}")
        print(Fore.RED + f"Error: {e}" + Fore.WHITE)
