no_args = False
args = ["dir"]
ids = ["cd", "chdir", "changedir"]
arg_type = "arg"
description = "change the working directory"

import os
from colorama.ansi import Fore


def run(dir):
    try:
        os.chdir(dir)
    except Exception as e:
        print(Fore.RED + e + Fore.WHITE)
