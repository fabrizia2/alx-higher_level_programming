#!/usr/bin/python3

"""Dscription to the read file func"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
