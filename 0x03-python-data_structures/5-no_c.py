#!/usr/bin/python3

def no_c(my_string):
    string = ""

    for con in my_string:
        if con == 'c' or con == 'C':
            pass
        else:
            string += con

    return string
