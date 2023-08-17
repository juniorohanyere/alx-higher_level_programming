#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    list = []

    for key, key_value in a_dictionary.items():
        if key_value is value:
            list.append(key)

    for key in list:
        del (a_dictionary[key])
    return (a_dictionary)
