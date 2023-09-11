#!/usr/bin/python3

'''
    4-inherits_from - defines a function inherits_from
'''


def inherits_from(obj, a_class):
    '''
        inherits_from - checks if the object is an instance of a class that
                        inherited directly or indirectly from a specific class

        Args:
            obj: the object
            a_class: the class

        Return: return True on success
                return False on failure

    '''

    return (type(obj) != a_class and isinstance(obj, a_class))
