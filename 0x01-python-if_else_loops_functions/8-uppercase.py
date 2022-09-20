#!/usr/bin/python3
def uppercase(str):
    for string in str:
        if 96 < ord(string) < 123:
            string = chr(ord(string) - 32)
        print("{}".format(string), end=' ')
