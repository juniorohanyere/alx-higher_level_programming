#!/usr/bin/python3

'''
    base - defines a base class function
'''


class Base:
    '''
        Base - a base class function
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
            __init__ - class constructor

            Args:
                id (int): id is assumed to be an integer

            Return: return nothing
        '''

        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
