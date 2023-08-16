#!/usr/bin/python3


'''
 ' uniq_add - function that adds all unique integers in a list
 '
 ' @my_list: the list
 '
 ' Description: addition is only once for each integer
 '
 ' Return: return the addition of the integers
'''


def uniq_add(my_list=[]):
    my_set = set(my_list)
    result = sum(my_set)

    return (result)
