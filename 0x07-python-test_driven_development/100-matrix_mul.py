#!/usr/bin/python3
'''
    multiples a matrix
    matrix multiplication!
'''


def matrix_mul(m_a, m_b):
    '''
        multiplies two matrices

        Args:
        m_a (nested list of ints/floats): the first matrix
        m_b (nested list of ints/floats): the second matrix
    '''

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elements, int) or isinstance(elements, float))
               for elements in [value for row in m_a for value in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(elements, int) or isinstance(elements, float))
               for elements in [value for row in m_b for value in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    trans_b = []
    for i in range(len(m_b[0])):
        r = []
        for j in range(len(m_b)):
            r.append(m_b[j][i])
        trans_b.append(r)

    m = []
    for row in m_a:
        r = []
        for column in trans_b:
            mul = 0
            for i in range(len(trans_b[0])):
                mul += row[i] * column[i]
            r.append(mul)
        m.append(r)

    return m
