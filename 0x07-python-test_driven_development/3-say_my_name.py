#!/usr/bin/python3

'''
    a module that prints
    the name of a person
    int full sentence
'''


def say_my_name(first_name, last_name=""):
    ''' prints My name is <first name> <last name>

        Args:
            first_name (str): the first name
            last_name (str and optional): the second name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
