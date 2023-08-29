#!/usr/bin/python3

''' square with size '''


class Square:
    ''' defines a square '''

    def __init__(self, size=0, position=(0, 0)):
        ''' define a square with a size

            Args:
                size (int): the size of the square
                position (int, int): the position of the square
        '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        ''' retrieves the position of the square '''

        return (self.__position)

    @position.setter
    def position(self, value):
        ''' sets the position for a square '''

        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise (TypeError(
                   "position must be a tuple of 2 positive integers"))
        self.__position = value

    def area(self):
        ''' area of the square '''

        return (self.__size ** 2)

    def my_print(self):
        ''' prints in stdout the square with the character # '''

        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print("")

    def __str__(self):
        ''' str method for how values should be printed to the stdout '''

        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")

        for i in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]

            if i != self.__size - 1:
                print("")

        return ("")
