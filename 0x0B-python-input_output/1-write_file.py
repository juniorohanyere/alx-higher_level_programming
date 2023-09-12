#!/usr/bin/python3

'''
    1-write_file - defines a function that writes to a file
'''


def write_file(filename="", text=""):
    '''
        write_file - writes a string to a text file

        Args:
            filename (str): the name of the file to write to (optional)
            text (str): the string to be written into @filename (optional)

        Return: return the number of characters written
    '''

    with open(filename, "w") as file:
        return (file.write(text))
