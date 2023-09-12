#!/usr/bin/python3

'''
    0-read_file.py - defines a function to read the content of a file
'''


def read_file(filename=""):
    '''
        read_file - reads a text file (utf-8) and prints it to the stdout

        Args:
            filename (str): the name of the file to read from (optional)

        Return: return nothing
    '''

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
