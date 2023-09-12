#!/usr/bin/python3
'''
    7-add_item - script that adds all arguments to a python list
'''

import sys


def add_item(str):
    '''
        add_item - adds all arguments to a list

        Args:
            str (str): contains the arguments

        Return: return nothing
    '''

    obj1 = __import__('5-save_to_json_file').save_to_json_file
    obj2 = __import__('6-load_from_json_file').load_from_json_file

    try:
        obj = obj2("add_item.json")

    except FileNotFoundError:
        obj = []

    obj.extend(str)
    obj1(obj, "add_item.json")


if __name__ == "__main__":
    add_item(sys.argv[1:])
