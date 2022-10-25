#!/usr/bin/python3

"""Description to the write file func"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)"""

    """Using with"""

    with open(filename, "w", encoding="utf-8") as f:
        """returns the number of characters written:"""
        return f.write(text)
