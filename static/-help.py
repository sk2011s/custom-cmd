import os
from sys import dont_write_bytecode
import logging
from colorama.ansi import Fore

dont_write_bytecode = True

args = []
arg_type = "args"
no_args = True
ids = ["help", "Help"]


@staticmethod
def run(commands):
    try:
        print("\n\nAvailable commands:\n")
        for module in set(commands.values()):
            if "help" in module.ids or "Help" in module.ids:
                continue  # Skip the help command
            cmd_ids = "/".join(module.ids)
            filename = os.path.basename(module.__spec__.origin).split(".")[0]
            print(f"Command: {filename}\n  Usage: {cmd_ids} [arguments]")
            if hasattr(module, "description"):
                print(f"  Description: {module.description}")
            print(f"  Arguments: {module.args}\n")
    except Exception as e:
        logging.error(f"Error displaying help: {e}")
        print(Fore.RED + f"Error displaying help: {e}" + Fore.WHITE)
