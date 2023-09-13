#!/usr/bin/python3

'''
    100-append_after - defines a function that appends a line of text to a file
'''


def append_after(filename="", search_string="", new_string=""):
    '''
        append_after -  inserts a line of text to a file, after each line
                        containing a specific string

        Args:
            filename (str): the name of the file
            search_string (str): the delimeter
            new_string (str): the line of text to insert

        Return: return nothing
    '''

    with open(filename, "r+") as file:
        i = 0
        lines = file.readlines()

        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)

            i += 1

        file.seek(0)
        file.write("".join(lines))
