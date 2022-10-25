#!/usr/bin/python3

"""Defination of from_json_string func"""
import json


def from_json_string(my_str):
    """ a function that returns an object represented by a JSON string"""
    return json.loads(my_str)
