#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """prints in ascending order"""
        print(sorted(self))
