#!/usr/bin/python3

'''
    2-is_same_class - defines a function is_same_class
'''


def is_same_class(obj, a_class):
    '''
        is_same_class - checks if an object is exactly an instance of a
                        specific class

        Args:
            obj: the object
            a_class: the class

        Return: return True on success
                return False on failure
    '''

    if type(obj) == a_class:
        return True

    return False
