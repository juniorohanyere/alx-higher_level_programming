#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return (None)

    i = 0
    while True:
        try:
            if i < x:
                print("{}".format(my_list[i]), end='')
                i += 1
            else:
                print()
                return (i)
        except IndexError:
            print()
            return (i)
