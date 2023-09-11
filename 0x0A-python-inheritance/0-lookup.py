#!/usr/bin/python3

'''
    function that returns the list of available attributes and methods of an
    object
'''


def lookup(obj):
    '''
        lookup - looks up an object

        Args:
            obj: the object to look up

        Return: return a list object
    '''

    return (dir(obj))
