#!/usr/bin/python3


'''
 ' simple_delete - function that deletes a key in a dictionary
 '
 ' @a_dictionary: the dictionary
 ' @key: the key (always a string)
 '
 ' Return: return the updated dictionary
'''


def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        pass    # do nothing
    else:
        del (a_dictionary[key])

    return (a_dictionary)
