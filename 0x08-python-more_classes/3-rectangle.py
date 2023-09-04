#!/usr/bin/python3
'''
    defines a rectangle
'''


class Rectangle:
    '''
        defines a rectangle by: (based on 2-rectangle.py)
    '''

    def __init__(self, width=0, height=0):
        '''
            intstantiate the values for the new rectangle object

            Args:
                width (int): width of the rectangle.
                height (int): height of the rectangle.
        '''

        self.height = height
        self.width = width

    @property
    def width(self):
        '''
            retrieves the width
        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''
            sets a value for the width

            Args:
                value (int): the value to assign to the width
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
            retrieves the value of the height
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
            sets a value to the height of the rectangle

            Args:
                value (int): the value to assign the the height
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            returns the area of a rectangle
        '''

        return (self.__height * self.__width)

    def perimeter(self):
        '''
            returns the perimeter of a rectangle
        '''

        if self.__height == 0 or self.__width == 0:
            return (0)

        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        '''
            returns the an informal and nicely printable format of the
            rectangle
        '''

        if self.__height == 0 or self.__width == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")

            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
