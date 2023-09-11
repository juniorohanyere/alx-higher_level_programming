#!/usr/bin/python3

'''
    101-add_attribute - defines a function that adds a new attribute to an
                        object
'''


def add_attribute(obj, att, value):
    '''
        add_attribute - adds a new attribute to an object if it is possible

        Args:
            obj: the object
            att: the attribute to be added to @obj
            value: the value of the @att

        Return: rasie a TypeError if impossible
    '''

    if not hasattr(obj, "__dict__"):
        raise (TypeError("can't add new attribute"))

    setattr(obj, att, value)
