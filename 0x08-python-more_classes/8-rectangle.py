#!/usr/bin/python3
'''
    defines a rectangle
'''


class Rectangle:
    '''
        defines a rectangle by: (based on 7-rectangle.py)
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
            intstantiate the values for the new rectangle object

            Args:
                width (int): width of the rectangle.
                height (int): height of the rectangle.
        '''

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
            returns the biggest rectangle based on the area

            Args:
                rect_1 (Rectangle): the first rectangle
                rect_2 (Rectangle): the second rectangle
        '''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

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

        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if self.__height > i + 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        '''
            returns a string representation of the rectangle
        '''

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        '''
            deletes a rectangle and prints a farewell message
        '''

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
