#!/usr/bin/python3

'''
    4-from_json_string - defines a json function
'''

import json


def from_json_string(my_str):
    '''
        from_json_string - from json string

        Args:
            my_str: the string

        Return: return an object (python data structure) represented by a json
                string
    '''

    return (json.loads(my_str))
