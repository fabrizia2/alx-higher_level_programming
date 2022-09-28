#!/usr/bin/python3

# Weighted average!
# Returns 0 if the list is empty

def weight_average(my_list=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix))
