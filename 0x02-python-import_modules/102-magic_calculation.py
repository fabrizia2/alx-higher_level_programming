#!/usr/bin/python3

def magic_calculation(a, b):
    from mgic_calculation_102 import add, sub
    if a < b:
        summ = add(a, b)
        for num in range(4, 6):
            summ = add(summ, num)
        return (summ)
    else:
        return (sub(a, b))
