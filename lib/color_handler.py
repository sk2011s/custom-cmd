from colorama.ansi import Fore
from sys import dont_write_bytecode

dont_write_bytecode = True

colors = {
    "&1E": Fore.BLACK,
    "&1F": Fore.RED,
    "&20": Fore.GREEN,
    "&21": Fore.YELLOW,
    "&22": Fore.BLUE,
    "&23": Fore.MAGENTA,
    "&24": Fore.CYAN,
    "&25": Fore.WHITE,
    "&27": Fore.RESET,
    "&5A": Fore.LIGHTBLACK_EX,
    "&5B": Fore.LIGHTRED_EX,
    "&5C": Fore.LIGHTGREEN_EX,
    "&5D": Fore.LIGHTYELLOW_EX,
    "&5E": Fore.LIGHTBLUE_EX,
    "&5F": Fore.LIGHTMAGENTA_EX,
    "&60": Fore.LIGHTCYAN_EX,
    "&61": Fore.LIGHTWHITE_EX,
}


def handle(txt: str) -> str:
    used = False
    for i in colors.keys():
        if i in txt:
            used = True
        txt = txt.replace(i, colors.get(i))
    if used:
        txt += Fore.RESET

    return txt
