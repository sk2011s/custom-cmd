import requests
import os
import json
from colorama.ansi import Fore
from sys import dont_write_bytecode
import logging

dont_write_bytecode = True

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

no_args = False
args = ["url"]
ids = ["git"]
arg_type = "arg"
description = "download command file from github"

with open("config.json", "r") as f:
    config = json.load(f)

@staticmethod
def run(url):
    local_filename = os.path.join(config["Commands_Folder"], os.path.basename(url))

    def download_file(url, local_filename):
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if all(
                            keyword in str(chunk)
                            for keyword in ["def run", "ids =", "args =", "no_args =", "description =", "arg_type ="]
                        ):
                            f.write(chunk)
                            print(Fore.GREEN + f"File downloaded as {local_filename}" + Fore.WHITE)
                        else:
                            print(Fore.YELLOW + "invalid file" + Fore.WHITE)
            return local_filename
        except Exception as e:
            logging.error(f"Error downloading file: {e}")
            print(Fore.RED + f"Error downloading file: {e}" + Fore.WHITE)
            return None

    if local_filename.endswith(".py"):
        download_file(url, local_filename)
    else:
        print(Fore.YELLOW + "file is not python file" + Fore.WHITE)
