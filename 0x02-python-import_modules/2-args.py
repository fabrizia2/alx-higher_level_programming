#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from sys import argv
    Argument = len(sys.argv) - 1

    if len(sys.argv) == 1:
        print("{} arguments".format(Argument))
    elif len(sys.argv) == 2:
        print("{} argument:".format(Argument))
    else:
        print("{} arguments:".format(Argument))

    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, argv[arg]))
