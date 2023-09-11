#!/usr/bin/python3

'''
    6-base_geometry - defines a base geometry class
'''


class BaseGeometry:
    '''
        BaseGeometry - a class based on 6-base_geometry.py
    '''

    def area(self):
        '''
            area - area of a geometry

            Return: raises an exception (area if not implemented)
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            integer_validator - validates values

            Args:
                name: always a string
                value: the value of @name (must be an integer)

            Return: raise TypeError if @value is not an integer
                    raise ValueError if @value is less than or equals zero
        '''

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
