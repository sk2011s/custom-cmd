import tkinter as tk
from tkinter import messagebox as msg
from os import path
from json import load
from sys import dont_write_bytecode
import logging
from colorama.ansi import Fore

dont_write_bytecode = True

with open("config.json", "r") as f:
    config = load(f)

no_args = False
args = []
ids = ["mnc"]
arg_type = "args"
description = ""


@staticmethod
def run():

    def rsubmit():
        if checkok(idse.get(), name.get(), description.get(), argse.get()) == 0:
            root.destroy()

    root = tk.Tk()
    root.title("mnc-gui")
    root.minsize(320, 240)
    root.resizable(False, False)

    tk.Label(root, text="Name:").pack()
    name = tk.Entry(root)
    name.pack()

    tk.Label(root, text="ids:").pack()
    tk.Label(root, text='split ids with ","', fg="gray").pack()

    idse = tk.Entry(root)
    idse.pack()

    tk.Label(root, text="args:").pack()
    tk.Label(root, text='split args with ","', fg="gray").pack()
    argse = tk.Entry(root)
    argse.pack()

    tk.Label(root, text="Description:").pack()
    description = tk.Entry(root)
    description.pack()

    submit = tk.Button(root, text="submit", command=lambda: rsubmit())
    submit.pack()

    root.mainloop()


def checkok(idsc, name, desc, args):
    if check(name=name, idsc=idsc, desc=desc, args=args):
        try:
            with open(path.join(config["Commands_Folder"], name + ".py"), "w") as f:
                f.write(
                    f"""^ 
no_args = False
args = {args.split(",")}
ids = {idsc.split(",")}
arg_type = "args"
description = "{desc}"

def run({args}):
    pass
""".replace(
                        "^\n", ""
                    )
                )
            return 0
        except Exception as e:
            logging.error(f"Failed to create command file: {e}")
            msg.showerror("Error", Fore.RED + f"Failed to create command file: {e}" + Fore.WHITE)
            return -1


def check(name: str, idsc: str, desc: str, args: str):
    if name != "" and desc != "" and idsc != "" and args != "":
        if name.startswith("-"):
            logging.error("Name Can't Start With '-'")
            msg.showerror("Error", Fore.RED + "Name Can't Start With '-'" + Fore.WHITE)
            return False

        if " " in idsc or " " in args:
            logging.error("Ids is Invalid")
            msg.showerror("Error", Fore.RED + "Ids is Invalid" + Fore.WHITE)
            return False
    else:
        logging.error("Please fill in all the entries")
        msg.showerror("Error", Fore.RED + "Please fill in all the entries" + Fore.WHITE)
        return False

    return True
