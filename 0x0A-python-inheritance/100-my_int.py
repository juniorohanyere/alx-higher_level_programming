#!/usr/bin/python3

'''
    10-my_int - defines a MyInt class that inherits from a int
'''


class MyInt(int):
    '''
        MyInt - inherits the properties of an int

        Args:
            int: the int
    '''

    def __eq__(self, value):
        '''
            == operator

            Args:
                value: the value of the int

            Return: return True if value is not real
                    return False if value is real
        '''

        return (self.real != value)

    def __ne__(self, value):
        '''
            != operator

            Args:
                value: the value of the int

            Return: return True if value is real
                    return False if value is not real
        '''

        return (self.real == value)
