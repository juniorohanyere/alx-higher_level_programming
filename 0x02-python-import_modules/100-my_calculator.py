#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def calculator(argv):
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./{:s} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argc == 3:
        if argv[2] == "+":
            result = add(a, b)

        elif argv[2] == "-":
            result = sub(a, b)

        elif argv[2] == "*":
            result = mul(a, b)

        elif argv[2] == "/":
            result = div(a, b)

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, result))


if __name__ == "__main__":
    calculator(sys.argv)
