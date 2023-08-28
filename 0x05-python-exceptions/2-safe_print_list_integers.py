#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0

    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end='')
                i += 1
                j += 1
            else:
                print()
                return (j)
        except (ValueError, TypeError):
            i += 1
