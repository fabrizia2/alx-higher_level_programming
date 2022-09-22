#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    c = add(a, b)
    print("{} + {} = {}".format(a, b, c))

    d = sub(a, b)
    print("{} - {} = {}".format(a, b, d))

    e = mul(a, b)
    print("{} * {} = {}".format(a, b, e))

    f = div(a, b)
    print("{} / {} = {}".format(a, b, f))
