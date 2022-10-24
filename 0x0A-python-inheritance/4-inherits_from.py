#!/usr/bin/python3
"""Direct or indirect inheritance"""


def inherits_from(obj, a_class):
    """Inheritance check"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
