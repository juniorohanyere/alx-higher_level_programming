#!/usr/bin/python3


'''
 ' update_dictionary - function that replaces or adds key/value in a dictionary
 '
 ' @a_dictionary: the dictionary
 ' @key: the key of the dictionary
 ' @value: the value of @key
 '
 ' Return: return the updated dictionary
'''


def update_dictionary(a_dictionary, key, value):
    a_dictionary.update([(key, value)])

    return (a_dictionary)
