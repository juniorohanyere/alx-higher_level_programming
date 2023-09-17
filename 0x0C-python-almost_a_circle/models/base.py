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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            save_to_file - writes the JSON string representation of a list
                           object to a file

            Args:
                cls: the class name
                list_objs: the list objects

            Return: return nothing
        '''

        filename = cls.__name__ + ".json"
        new_string = []

        if list_objs is not None:
            for list_item in list_objs:
                list_item = list_item.to_dictionary()
                json_rep = json.loads(cls.to_json_string(list_item))
                new_string.append(json_rep)

        with open(filename, 'w') as file:
            json.dump(new_string, file)
