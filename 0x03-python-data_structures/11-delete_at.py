#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)

    length = len(my_list)
    new_list = []

    for i in range(0, length):
        if i != idx:
            new_list.append(my_list[i])

    my_list[:] = new_list

    return (my_list)
