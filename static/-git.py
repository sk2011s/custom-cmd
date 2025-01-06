import requests
import os
import json

no_args = False
args = ["url"]
ids = ["git"]
arg_type = "args"
description = "download command file from github"

with open("config.json", "r") as f:
    config = json.load(f)
    f.close()

@staticmethod
def run(url, *args):

    local_filename = os.path.join(config["Commands_Folder"], os.path.basename(url))

    def download_file(url, local_filename):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if (
                        "def run" in str(chunk)
                        and "ids =" in str(chunk)
                        and "args =" in str(chunk)
                        and "no_args =" in str(chunk)
                        and "description =" in str(chunk)
                        and "arg_type =" in str(chunk)
                    ):
                        f.write(chunk)
                        print(f"File downloaded as {local_filename}")
                    else:
                        print("invalid file")
        return local_filename

    if local_filename.endswith(".py"):
        download_file(url, local_filename)
        return -1
    else:
        print("file is not python file")
        


if __name__ == "__main__":
    run()
