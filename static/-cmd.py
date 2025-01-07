from os import system as bat
from colorama.ansi import Fore

no_args = False
args = ["command"]
ids = ["cmd"]
arg_type = "arg"
description = "run cmd command"


@staticmethod
def run(*args):
    try:
        # Joining arguments into a single command string
        command = " ".join(args)
        #        print(f"Executing command: {command}")
        bat(command)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.WHITE)
