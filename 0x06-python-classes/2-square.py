#!/usr/bin/python3

''' square with size '''


class Square:
    ''' defines a square '''

    def __init__(self, size=0):
        ''' define a square

            Args:
                size (int): the size of the square
        '''

        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))

        elif size < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = size
