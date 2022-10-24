#!/usr/bin/python3
"""Defines instance class"""


def is_kind_of_class(obj, a_class):
    """Checking for instance classes"""

    if not isinstance(obj, a_class):
        return False
    return True
