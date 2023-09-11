#!/usr/bin/python3
'''
    defines a square rectangle class
'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        square rectangle class

        Args:
            Rectangle: a rectangle object
    '''

    def __init__(self, size):
        '''
            initialiser
        '''

        self.__size = size
        super().__init__(self.__size, self.__size)
