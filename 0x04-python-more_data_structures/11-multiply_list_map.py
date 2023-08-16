#!/usr/bin/python3


'''
 ' multiply_list_map - function that returns a list with all values multiplied
 '                     by a number without using any loops
 '
 ' @my_list: the list
 ' @number: the number
 '
 ' Return: return a new list
'''


def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x: x * number, my_list)))
