#!/usr/bin/python3


'''
 ' best_score - function that returns a key with the biggest integer value
 '
 ' @a_dictionary: the dictionary
 '
 ' Return: return the key with the highest integer value
'''


def best_score(a_dictionary):
    max = 0

    if a_dictionary is None:
        return None

    for key in a_dictionary:
        value = a_dictionary.get(key)
        if value > max:
            max = value
            key_max = key

    return (key_max)
