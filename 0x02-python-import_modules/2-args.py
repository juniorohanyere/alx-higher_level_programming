#!/usr/bin/python3

import sys


def args(argv):
    nargs = len(argv)
    argc = nargs - 1

    if argc == 0:
        print("{:d} arguments.".format(argc))

    elif argc == 1:
        print("{:d} argument:".format(argc))
        print("{:d}: {:s}".format(argc, argv[argc]))

    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    args(sys.argv)
