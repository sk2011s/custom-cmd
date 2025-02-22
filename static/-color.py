from os import system as bat
from sys import dont_write_bytecode
import logging

dont_write_bytecode = True

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

no_args = False
args = ["color"]
ids = ["color"]
arg_type = "arg"
description = "change the color of ccmd (use cmd colors)"

@staticmethod
def run(color: str) -> None:
    bat(f"color {color}")
