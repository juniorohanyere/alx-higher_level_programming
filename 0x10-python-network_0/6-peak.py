#!/usr/bin/python3
"""peak module that uses the lowest complexity
"""


def find_peak(list_of_integers):
    """finds the peak of a given list of integers

    Args:
        list_of_integers (list): the given list of integer

    Return:
        return the peak value if the list is not empty
        return None otherwise
    """

    if list_of_integers == []:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
