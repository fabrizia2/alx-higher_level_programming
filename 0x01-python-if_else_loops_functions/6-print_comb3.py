#!/usr/bin/python3
for comb in range(0, 9):
    for two in range(comb + 1, 10):
        if comb == 8:
            print("{}{}".format(comb, two))
        else:
            print("{}{}".format(comb, two), end=", ")
