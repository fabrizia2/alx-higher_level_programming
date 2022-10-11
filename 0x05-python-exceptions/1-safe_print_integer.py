#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:}".format(value), end="")
        print()
    except (ValueError, TypeError):
        return False
    else:
        return True
