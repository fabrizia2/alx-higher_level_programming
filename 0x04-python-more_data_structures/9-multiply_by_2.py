#!/usr/bin/python3

# Multiply by 2
# You can assume that all values are only integers
# Returns a new dictionary

def multiply_by_2(a_dictionary):
    new = {}
    for mul in a_dictionary:
        new[mul] = a_dictionary[mul] * 2

    return new
