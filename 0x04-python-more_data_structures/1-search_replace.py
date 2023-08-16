#!/usr/bin/python3


'''
 ' search_replace - function that replaces all occurences of an element by
 '                  another in a new list
 '
 ' @my_list: the initial list
 ' @search: the element to replace in the list
 ' @the new element
 '
 ' Return: return a new list with the replaced element
'''


def search_replace(my_list, search, replace):
    new_list = []
    length = len(my_list)

    for i in range(0, length):
        if search == my_list[i]:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])

    return (new_list)
