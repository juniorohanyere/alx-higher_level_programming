#!/usr/bin/python3

'''
    rectangle - defines a rectangle class that inherits from Base
'''

from models.base import Base


class Rectangle(Base):
    '''
        Rectangle - a rectangle class that inherits from a Base class

        Args:
            Base: the parent class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            __init__ - class constructor

            Args:
                width (int): the width of a rectangle
                height (int): the height of a rectangle
                x (int): the horizontal starting offset
                y (int): the vertical starting offset
                id (int): the id of the rectangle

            Return: return nothing
        '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        '''
            width - retrieves the value of the width of a rectangle

            Return: return the width of the rectangle
        '''

        return (self.__width)

    @width.setter
    def width(self, value):
        '''
            width - assigns a value to the width of a rectangle

            Args:
                value (int): the value of the width of the rectangle

            Return: return nothing
        '''

        self.is_valid("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            height - retrieves the value of the height of a rectangle

            Return: return the height of the rectangle
        '''

        return (self.__height)

    @height.setter
    def height(self, value):
        '''
            height - assigns a value to the height of a rectangle

            Args:
                value (int): the value to assign

            Return: return nothing
        '''

        self.is_valid("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            x - retrieves the value of the horizonatal offset of a rectangle

            Return: return the horizontal offset of the rectangle
        '''

        return (self.__x)

    @x.setter
    def x(self, value):
        '''
            x - assigns a value to the horizontal offset of a rectangle

            Args:
                value (int): the value to assign

            Return: return nothing
        '''

        self.is_valid("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            y - retrieves the value of the vertical offset of a rectangle

            Return: return the vertical offset of the rectangle
        '''

        return (self.__y)

    @y.setter
    def y(self, value):
        '''
            y - assigns a value to the vertical offset of a rectangle

            Args:
                value (int): the value to assign

            Return: return nothing
        '''

        self.is_valid("y", value)
        self.__y = value

    @staticmethod
    def is_valid(name, value):
        '''
            is_valid - validates the value of a setter

            Args:
                name (str): name of the setter function
                value (int): value of the setter

            Return: raise TypeError if @value is not an integer
                    raise ValueError if width or height is under or equals zero
                    raise ValueError if x or y is under zero
        '''

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{:s} must be > 0".format(name))

        elif value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        '''
            area - area of a rectangle (l * b)

            Return: return the area of a rectangle
        '''

        return (self.__width * self.__height)

    def display(self):
        '''
            display - prints in stdout the Rectangle instance with the
                      the character #

            Return: return nothing
        '''

        rect = ""

        print("\n" * self.__y, end='')

        for i in range(self.__height):
            rect += (" " * self.__x) + ("#" * self.__width) + "\n"

        print(rect, end='')

    def __str__(self):
        '''
            __str__ - prints in str format (override the original str mathod

            Return: return some other string
        '''

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                                                          self.id, self.__x,
                                                          self.__y,
                                                          self.__width,
                                                          self.__height)
