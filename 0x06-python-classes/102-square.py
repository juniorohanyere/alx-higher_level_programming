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
        ''' retrieves the size of square '''

        return (self.__size)

    @size.setter
    def size(self, value):
        ''' sets the size for a square

            Args:
                value (int): the value of the size to set
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        ''' area of the square '''

        return (self.__size ** 2)

    def __eq__(self, other):
        ''' comparision to a Square (==)

            Args:
                other: other
        '''

        return (self.area() == other.area())

    def __ne__(self, other):
        ''' comparison to a Square definition

            Args:
                other: other
        '''

        return (self.area() != other.area())

    def __lt__(self, other):
        ''' comparison to a Square (<)

            Args:
                other: other
        '''

        return (self.area() < other.area())

    def __le__(self, other):
        ''' comparison to a Square (<=)

            Args:
                other: other
        '''

        return (self.area() <= other.area())

    def __gt__(self, other):
        ''' comparison to a Square (>)

            Args:
                other: other
        '''

        return (self.area() > other.area())

    def __ge__(self, other):
        ''' compmarison to a Square (>=)

            Args:
                other: other
        '''

        return self.area() >= other.area()
