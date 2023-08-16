#!/usr/bin/python3


'''
 ' print_sorted_dictionary - function that prints a dictionary by ordered keys
 '
 ' @a_dixtionary: the dictionary
 '
 ' Return: return nothing
'''


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:s}: {}".format(key, a_dictionary.get(key)))
