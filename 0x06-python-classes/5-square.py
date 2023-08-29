#!/usr/bin/python3

''' square with size '''


class Square:
    ''' defines a square '''

    def __init__(self, size=0):
        ''' define a square with a size

            Args:
                size (int): the size of the square
        '''

        self.size = size

    @property
    def size(self):
        ''' retrieves size of square '''

        return (self.__size)

    @size.setter
    def size(self, value):
        ''' sets the size for a square

            Args:
                value (int): the value of the size to set
        '''

        if not isinstance(value, int):
            raise (TypeError("size must be an integer"))

        elif value < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = value

    def area(self):
        ''' area of the square '''

        return (self.__size ** 2)

    def my_print(self):
        ''' prints in stdout the square with the character # '''

        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
