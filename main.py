import os
import shlex
from lib.commands import load_commands
import inspect
from lib.variable_handler import environment_var
import json
import logging
import datetime

import sys
sys.dont_write_bytecode = True

os.system("cls")


# run command function
def execute_command(commands, help_ids, command_id, *args):
    try:
        if command_id in commands:
            command = commands[command_id]
            sig = inspect.signature(command.run)
            params = list(sig.parameters.values())
            required_params = [
                p
                for p in params
                if p.default == inspect.Parameter.empty
                and p.kind
                in (
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    inspect.Parameter.POSITIONAL_ONLY,
                )
            ]
            if len(args) < len(required_params) and not command.no_args:
                print(
                    f"Error: Too few arguments for command '{command_id}'. Expected {len(required_params)}, got {len(args)}."
                )
                print(f"run {help_ids}")
                return 0
            elif len(args) > len(params) and (not(command.no_args or str(command.arg_type) == "arg")):
                print(
                    f"Error: Too many arguments for command '{command_id}'. Expected {len(params)}, got {len(args)}."
                )
                print(f"run {help_ids}")
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
            print(f'Command "{command_id}" not found.')
            logging.error(f"command {command_id} not found")
            return 0
    except Exception as e:
#        print(f"Error executing command '{command_id}': {e}")
        logging.error(f"Error executing command '{command_id}': {e}")
        os._exit(-1)
        return 0


with open("config.json", "r") as f:
    config = json.load(f)

logging.basicConfig(filename=os.path.join(config["log_folder"], f"\"{str(datetime.datetime.now())}\""+".log"), level=logging.DEBUG)

# save loaded commands
commands, help_ids = load_commands(
    config["Commands_Folder"], os.getcwd() + "\\static_commands"
)

# main loop
while True:
    try:
        user_input = input(f"{os.getcwd()}>")
        user_input = environment_var(user_input)
        parts = shlex.split(user_input)
        command_id = parts[0]
        args = parts[1:]

        result = execute_command(commands, help_ids, command_id, *args)
        #        print(result)
        if result == -1:
            break
    except Exception as e:
#        print(f"Error in main loop: {e}")
        logging.error(f"Error in main loop: {e}")
        os._exit(-1)
