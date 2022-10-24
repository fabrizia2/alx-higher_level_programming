#!/usr/bin/python3
"""Defines the function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""

    if type(obj) != a_class:
        return False
    return True
