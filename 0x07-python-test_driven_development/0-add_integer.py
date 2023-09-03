#!/usr/bin/python3

'''
    a module
    to add
    two operands together
'''


def add_integer(a, b=98):
    ''' adds two operands together if they're either integer or float
        otherwise raise a type error exception

        Args:
            a (int or float): the first operand
            b (int or float): the second operand (optional)
    '''

    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or
       isinstance(b, float)):
        return (int(a) + int(b))
    elif not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
