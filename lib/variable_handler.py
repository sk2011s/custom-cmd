from os import environ
from sys import dont_write_bytecode

dont_write_bytecode = True

env_var = [f"{var}^{val}" for var, val in environ.items()]

def environment_var(text: str) -> str:
    txt = text
    for i in env_var:
        var = str(i).lower().split("^")
        if f"%{var[0]}%" in txt:
            txt = txt.replace(f"%{var[0]}%", var[1].replace("\\", "\\\\"))
    return rf"{txt}"
