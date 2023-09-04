#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        defines unittests for max_integer([..])

        Args:
            unittest.Testcase: for making the test
    '''

    def ordered_list(self):
        '''
            ordered list
        '''

        olist = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(olist), 6)

    def unordered_list(self):
        '''
            unordered list
        '''

        ulist = [1, 2, 4, 3, 6, 5]
        self.assertEqual(max_integer(ulist), 6)

    def descending_list(self):
        '''
            descending list
        '''

        dlist = [6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(dlist), 6)

    def empty_list(self):
        '''
            test for empty list
        '''

        elist = []
        self.assertEqual(max_integer(elist), None)

    def single_element(self):
        '''
            test for list with only one element
        '''

        slist = [6]
        self.assertEqual(max_integer(slist), 6)

    def floats(self):
        '''
            test for floating point numbers
        '''

        flist = [1.63, 6.3, 7.12, -5.2, 16.2]
        self.assertEqual(max_integer(flist), 16.2)

    def int_floats(self):
        '''
            test for both int and float
        '''

        ilist = [12., 1.5, -7, 13.1, 6]
        self.assertEqual(max_integer(ilist), 13.1)

    def string(self):
        '''
            test for a string
        '''

        str = "Brennan"
        self.assertEqual(max_integer(str), 'a')

    def strings(self):
        '''
            test for a list of strings
        '''

        strings = ["Junior", "Ohanyere", "TwinJ", "Venetius"]
        self.assertEqual(max_integer(strings), "Junior")

    def empty_string(self):
        '''
            test for empty string
        '''

        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()
