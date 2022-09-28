#!/usr/bin/python3

# Weighted average!
# Returns 0 if the list is empty

def weight_average(my_list=[]):
    if not my_list:
        return 0

    aver = 0
    num = 0

    for weigh in my_list:
        aver += weigh[0] * weigh[1]
        num += weigh[1]

    return (aver / num)
