#!/usr/bin/python3
from sys import argv
if len(argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    operators = ['+', '/', '*', '-']
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

# changing variables to integers
    first = int(argv[1])
    second = int(argv[3])

    if argv[2] == '+':
        summ = add(first, second)
        print("{} + {} = {}".format(first, second, summ))

    if argv[2] == '/':
        quotient = div(first, second)
        print("{} / {} = {}".format(first, second, quotient))

    if argv[2] == '-':
        difference = sub(first, second)
        print("{} - {} = {}".format(first, second, difference))

    if argv[2] == '*':
        product = mul(first, second)
        print("{} * {} = {}".format(first, second, product))
