#!/usr/bin/python3

'''
    12-pascal_triangle - defines a pascal triangle function
'''


def pascal_triangle(n):
    '''
        pascal_triangle - Pascal's triangle representation

        Args:
            n (int): an integer

        Return: return a list of lists of integers representing the Pascal's
                triangle of @n
    '''

    if n <= 0:
        return ([])

    plist = [[1]]

    while (len(plist) != n):
        elist = plist[-1]
        element = [1]

        for i in range(len(elist) - 1):
            element.append(elist[i] + elist[i + 1])

        element.append(1)
        plist.append(element)

    return (plist)
