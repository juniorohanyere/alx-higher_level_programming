#!/usr/bin/python3


'''
 ' multiply_by_2 - function that returns a new dictionary with all values
 '                 multiplied by 2
 '
 ' @a_dictionary: the dictionary
 '
 ' Return: return a new dictionary
'''


def multiply_by_2(a_dictionary):
    new_dictionary = {}

    for key in a_dictionary:
        new_dictionary.update([(key, a_dictionary.get(key) * 2)])

    return (new_dictionary)
