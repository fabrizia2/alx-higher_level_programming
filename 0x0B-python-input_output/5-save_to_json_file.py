#!/usr/bin/python3

"""Intro to save_to_json_filefunc"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file"""

    """Using with"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
