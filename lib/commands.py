import importlib.util
from os import listdir, _exit, path
import logging, datetime, json
from colorama.ansi import Fore
from sys import dont_write_bytecode

dont_write_bytecode = True

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    logging.error("config.json file not found.")
    _exit(-1)
except json.JSONDecodeError:
    logging.error("Error decoding config.json.")
    _exit(-1)
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    _exit(-1)

log_filename = path.join(
    config["log_folder"], datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".log"
)
logging.basicConfig(filename=log_filename, level=logging.DEBUG)

def load_commands(directory, static_cmds):
    commands = {}
    help_ids = []
    print(Fore.BLUE + "loading commands..." + Fore.WHITE)
    try:
        files = listdir(directory) + listdir(static_cmds)
    except FileNotFoundError as e:
        logging.error(f"Directory not found: {e}")
        print(Fore.RED + f"Directory not found: {e}" + Fore.WHITE)
        _exit(-1)
    except Exception as e:
        logging.error(f"Error listing directories: {e}")
        print(Fore.RED + f"Error listing directories: {e}" + Fore.WHITE)
        _exit(-1)
    try:
        for filename in files:
            if filename.endswith(".py"):
                filepath = path.join(directory if not filename.startswith("-") else static_cmds, filename)
                spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for cmd_id in module.ids:
                    commands[cmd_id] = module
                if "help" in module.ids or "Help" in module.ids:
                    help_ids.extend(module.ids)
                print(Fore.GREEN + f"{filename} Loaded" + Fore.WHITE)
                logging.info(f"Loaded {filename}")
    except Exception as e:
        logging.error(f"Error loading commands: {e}")
        print(Fore.RED + f"Error loading commands: {e}" + Fore.WHITE)
        _exit(-1)
    return commands, help_ids
