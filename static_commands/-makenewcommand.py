from os import path
import json

no_args = True
args = []
arg_type = "args"
ids = ["mnc"]
description = "create a new command"

with open("config.json", "r") as f:
    config = json.load(f)

@staticmethod
def run():
    
    command_name = str(input("Enter name: "))
    command_id = str(input("Enter ids: ")).split(",")
    
    with open(path.join(config["Commands_Folder"], command_name + ".py"), "w") as f:
        f.write(
f"""^
no_args = False
args = []
ids = {command_id}
arg_type = "args"
description = ""

def run():
    pass
"""
.replace("^\n", ""))
        f.close()