#!/usr/bin/python3

'''
    this module prints a square
    to the standard output
    using the '#' character
'''


def print_square(size):
    ''' function that prints a square with the character #

        Args:
            size (int): is the size length of the square
    '''

    if not isinstance(size, int):
        raise (TypeError("size must be an integer"))
    if size < 0:
        raise (ValueError("size must be >= 0"))

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
