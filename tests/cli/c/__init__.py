import click
from clickd import clickd
from pathlib import Path
import os

@clickd(dpath="./tests/cli/c")
def c():
    pass