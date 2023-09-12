#!/usr/bin/python3

'''
    3-to_json_string - defines a json function
'''

import json


def to_json_string(my_obj):
    '''
        to_json_string - json string

        Args:
            my_obj: the object

        Return: returns the JSON representation of an object(string)
    '''

    return (json.dumps(my_obj))
