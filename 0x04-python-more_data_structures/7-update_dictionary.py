#!/usr/bin/python3

# @key argument will be always a string
# @value argument will be any type
# If a key exists in the dictionary, the value will be replaced
# If a key doesn’t exist in the dictionary, it will be created

def update_dictionary(a_dictionary, key, value):
    for val in a_dictionary:
        if val == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
