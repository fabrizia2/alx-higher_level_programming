#!/usr/bin/python3

"""Description of the append write func"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)"""

    """Using with"""
    with open(filename, "a", encoding="utf-8") as f:
        """returns the number of characters added"""

        returns f.write(text)
