#!/usr/bin/python3

# a function that adds all unique integers in a list

def uniq_add(my_list=[]):
    if not my_list:
        return 0

    new = set(my_list)
    summ = 0
    for i in new:
        summ += i

    return summ
