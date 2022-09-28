#!/usr/bin/python3

# Print sorted dictionary

def print_sorted_dictionary(a_dictionary):
    if not a_dictonary:
        return

    for key in sorted(a_dictonary.keys()):
        print("{}: {}".format(key, a_dictonary[ke]))
