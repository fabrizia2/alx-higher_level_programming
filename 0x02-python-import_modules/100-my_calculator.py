#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = ['+', '*', '-', '/']
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

# changing variables to integers
    first = int(argv[1])
    second = int(argv[3])

    if argv[2] == '*':
        prod = mul(first, second)
        print("{} * {} = {}".format(first, second, prod))

    elif argv[2] == '/':
        quotient = div(first, second)
        print("{} / {} = {}".format(first, second, quotient))

    elif argv[2] == '-':
        difference = sub(first, second)
        print("{} - {} = {}".format(first, second, difference))

    else:
        summ = add(first, second)
        print("{} + {} = {}".format(first, second, summ))
