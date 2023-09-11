#!/usr/bin/python3

'''
    8-rectangle - defines an inheritance class
'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Rectangle - a class that inherits from a parent class

        Args:
            BaseGeometry: the parent class
    '''

    def __init__(self, width, height):
        '''
            __init__ - the initialiser

            Args:
                width: the width of the rectangle
                height: the height of the rectangle

            Return: return nothing
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height= height
