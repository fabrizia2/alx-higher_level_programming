#!/usr/bin/python3

# a function that returns a set of common elements in two sets

def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return {}

    comel = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                comel.add(j)

    return comel
