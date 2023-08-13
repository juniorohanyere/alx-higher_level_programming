#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ")
        print()
