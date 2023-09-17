#!/usr/bin/python3

'''
    base - defines a base class function
'''

import json


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

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''
            to_json_string - gets the json string representation of a list

            Args:
                list_dictionaries (list): a list of dictionaries

            Return: return the json string representation fo @list_dictionaries
        '''

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
