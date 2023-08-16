#!/usr/bin/python3


'''
 ' only_diff_elements - function that returns a set of all elements present in
 '                      only one set
 '
 ' @set_1: the first set
 ' @set_2: the second set
 '
 ' Return: return a set of elements in @set_1 or @set_2 but not in both
'''


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
