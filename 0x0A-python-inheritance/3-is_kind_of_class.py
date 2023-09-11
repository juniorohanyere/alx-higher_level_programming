#!/usr/bin/python3

'''
    3-is_kind_of_class - defines a function is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
        is_kind_of_class - checks if an object is an instance of, or if the
                           object is an instance of a class that inherited from
                           the specified class

        Args:
            obj: the object
            a_class: the class

        Return: return True on success
                return False on failure
    '''

    return (isinstance(obj, a_class))
