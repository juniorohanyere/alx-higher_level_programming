#!/usr/bin/python3

'''
    2-append_write - defines a function that appends text at the end of a file
'''


def append_write(filename="", text=""):
    '''
        append_write - appends a text at the end of a file

        Args:
            filename (str): the name of the file (optional)
            text (str): the text to append

        Return: return the number of characters added
    '''

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
