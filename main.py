from os import getcwd, path, system, _exit
import shlex
from lib.commands import load_commands
import inspect
from lib.variable_handler import environment_var
from lib.color_handler import handle
from json import load, JSONDecodeError
import logging
from datetime import datetime
from colorama.ansi import Fore
from sys import dont_write_bytecode

dont_write_bytecode = True

system("cls")

def execute_command(commands, help_ids, command_id, *args):
    try:
        if command_id in commands:
            command = commands[command_id]
            sig = inspect.signature(command.run)
            params = list(sig.parameters.values())
            required_params = [
                p for p in params
                if p.default == inspect.Parameter.empty
                and p.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.POSITIONAL_ONLY)
            ]
            if len(args) < len(required_params) and not command.no_args:
                print(Fore.YELLOW + f"Too few arguments for command '{command_id}'. Expected {len(required_params)}, got {len(args)}." + Fore.WHITE)
                print(f"run {help_ids}")
                return 0
            elif len(args) > len(params) and not (command.no_args or str(command.arg_type) == "arg"):
                print(Fore.YELLOW + f"Too many arguments for command '{command_id}'. Expected {len(params)}, got {len(args)}." + Fore.WHITE)
                print(Fore.BLUE + f"run {help_ids}" + Fore.WHITE)
                return 0
            if not command.no_args:
                if command_id in help_ids:
                    logging.info(f"user used {command_id} by args:{str(*args)}")
                    return command.run(commands)
                else:
                    logging.info(f"user used {command_id} by args:{" ".join(args)}")
                    return command.run(*args)
            else:
                if command_id in help_ids:
                    logging.info(f"user used {command_id}".format(command_id))
                    return command.run(commands)
                else:
                    logging.info(f"user used {command_id}")
                    return command.run()
        else:
            print(Fore.YELLOW + f'Command "{command_id}" not found.' + Fore.WHITE)
            logging.warning(f"command {command_id} not found")
            return 0
    except Exception as e:
        logging.error(f"Error executing command '{command_id}': {e}")
        print(Fore.RED + f"Error executing command '{command_id}': {e}" + Fore.WHITE)
        _exit(-1)
        return 0

try:
    with open("config.json", "r") as f:
        config = load(f)
    print(Fore.GREEN + "config loaded successful" + Fore.WHITE)
    logging.info("config loaded successful")
except FileNotFoundError:
    logging.error("config.json file not found")
    print(Fore.RED + "config.json file not found" + Fore.WHITE)
    _exit(-1)
except JSONDecodeError as e:
    logging.error(f"Error decoding config.json: {e}")
    print(Fore.RED + f"Error decoding config.json: {e}" + Fore.WHITE)
    _exit(-1)
except Exception as e:
    logging.error(f"Unexpected error loading config.json: {e}")
    print(Fore.RED + f"Unexpected error loading config.json: {e}" + Fore.WHITE)
    _exit(-1)

system("cls")
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=path.join(config["log_folder"], f'"{str(datetime.now())}"' + ".log"),
    level=logging.DEBUG,
)

commands, help_ids = load_commands(config["Commands_Folder"], getcwd() + "\\static")
system("cls")

while True:
    try:
        user_input = input(f"{getcwd()}>")
        if user_input:
            user_input = environment_var(user_input)
            user_input = handle(user_input)
            parts = shlex.split(user_input)
            command_id = parts[0]
            args = parts[1:]

            result = execute_command(commands, help_ids, command_id, *args)

            if result == -1:
                del result, commands, help_ids, config
                _exit(0)
    except Exception as e:
        logging.error(f"Error in main loop: {e}")
        print(Fore.RED + f"Error in main loop: {e}" + Fore.WHITE)
        _exit(-1)
