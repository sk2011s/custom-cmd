import os
args = []
arg_type = "args"
no_args = True
ids = ["help", "Help"]

@staticmethod
def run(commands):
    print("\n\n")
    print("Available commands:")
    print("\n")
    for module in set(commands.values()):
        if "help" in module.ids or "Help" in module.ids:
            continue  # Skip the help command
        cmd_ids = "/".join(module.ids)
        filename = os.path.basename(module.__spec__.origin).split(".")[0]
        print(f"Command: {filename}")
        print(f"  Usage: {cmd_ids} [arguments]")
        if hasattr(module, "description"):
            print(f"  Description: {module.description}")
        print(f"  Arguments: {module.args}")
        print()
