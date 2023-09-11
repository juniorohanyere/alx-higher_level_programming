#!/usr/bin/python3

'''
    1-my_list - defines a class that inherits from a list
'''


class MyList(list):
    '''
        MyList - class that inherits from a list

        Args:
            list: a list
    '''

    def print_sorted(self):
        '''
            print_sorted - prints @list in sorted ascending order

            Return: return nothing
        '''

        print(sorted(self))
