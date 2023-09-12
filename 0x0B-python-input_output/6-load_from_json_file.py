#!/usr/bin/python3

'''
    6-load_from_json_file - defines a load from json function
'''

import json


def load_from_json_file(filename):
    '''
        load_from_json_file - creates an object from a json file

        Args:
            filename (str): the name of the json file

        Return: return the object created
    '''

    with open(filename) as file:
        return (json.load(file))
