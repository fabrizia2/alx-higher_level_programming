#!/usr/bin/python3

"""Intro to load_from_json_file func"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file” """

    """Using with"""

    with open(filename) as f:
        return json.load(f)
