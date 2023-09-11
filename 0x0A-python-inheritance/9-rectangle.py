#!/usr/bin/python3
'''
    defines a base geometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        definition of a Rectangle

        Args:
            BeseGeometry: parent class
    '''
    def __init__(self, width, height):
        '''
            constructor for width and height
        '''

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        '''
            print in string format
        '''

        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
