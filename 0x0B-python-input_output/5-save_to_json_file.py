#!/usr/bin/python3

'''
    5-save_to_json_file - defines a json function
'''

import json


def save_to_json_file(my_obj, filename):
    '''
        save_to_json_file - writes an object to a text file using JSON
                            representation

        Args:
            my_obj: the object
            filename (str): the name of the text file

        Return: return nothing
    '''

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
