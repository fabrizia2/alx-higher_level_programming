#!/usr/bin/python3

# a function that returns a set of all elements present in only one set

def only_diff_elements(set_1, set_2):
    if not set_1 or not set_2:
        return {}

    diff = set()
    for i in set_1:
        for j in set_2:
            if i != j:
                diff.add(j)

    return diff
