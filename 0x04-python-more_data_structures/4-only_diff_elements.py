#!/usr/bin/python3

# a function that returns a set of all elements present in only one set

def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return {}

    return (set_1 ^ set_2)
