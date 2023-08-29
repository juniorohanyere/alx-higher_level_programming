#!/usr/bin/python3

''' square with size '''


class Square:
    ''' defines a square '''

    def __init__(self, size=0):
        ''' define a square with a size

            Args:
                size (int): the size of the square
        '''

        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))

        elif size < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = size

    def area(self):
        ''' area of the square '''

        return (self.__size ** 2)
