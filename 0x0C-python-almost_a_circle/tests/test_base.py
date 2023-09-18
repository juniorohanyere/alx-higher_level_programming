#!/usr/bin/python3
'''
    test_base - unittests for ../models/base.py
'''

import unittest
from models.square import Square
import sys
from io import StringIO
import pep8
from models.base import Base
import json
from models.rectangle import Rectangle
import os


class TestBase(unittest.TestCase):
    '''
        TestBase - class to test the Base class in ../models/base.py

        Args:
            unittest.TestCase: performs the test
    '''

    def setup(self):
        '''
            setup  - redirects stdout

            Return: return nothing
        '''

        sys.stdout = StringIO()

    def teardown(self):
        '''
            teardown - flushes stdout

            Return: return nothing
        '''

        sys.stdout = sys.__stdout__

    def docstring(self):
        '''
            docstring - tests docstrings

            Return: return nothing
        '''

        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_id(self):
        '''
            test_id - tests for id's

            Return: return nothing
        '''

        Base._Base__nb_objects = 0
        base = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base(12)
        base5 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 12)
        self.assertEqual(base5.id, 4)

    def test_from_json_string(self):
        '''
            test_from_json_string - tests the from json string function

            Return: return nothing
        '''

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            rect = Rectangle(10, 7, 2, 8, 1)
            rect_dict = rect.to_dictionary()
            json_dict = Base.to_json_string([rect_dict])
            self.assertEqual(rect_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(rect_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))

    def test_rect(self):
        '''
            test_rect - tests the Rectangle function

            Return: return nothing
        '''

        rect = Rectangle(4, 5, 6)
        rect_dict = rect.to_dictionary()
        rect2 = Rectangle.create(**rect_dict)
        self.assertNotEqual(rect, rect2)

    def test_square(self):
        '''
            test_square - tests the Square function

            Return: return nothing
        '''

        sq = Square(44, 55, 66, 77)
        sq_dict = sq.to_dictionary()
        sq2 = Rectangle.create(**sq_dict)
        self.assertNotEqual(sq, sq2)

    def test_frect(self):
        '''
            test_frect - tests rectangle.py file

            Return: return nothing
        '''

        rect = Rectangle(33, 34, 35, 26)
        rect2 = Rectangle(202, 2)
        frect = [rect, rect2]
        Rectangle.save_to_file(frect)
        frect2 = Rectangle.load_from_file()
        self.assertNotEqual(frect, frect2)

    def test_fsquare(self):
        '''
            test_fsquare - checks if file loads from square

            Return: return nothing
        '''

        sq = Square(22)
        sq2 = Square(44, 44, 55, 66)
        fsq = [sq, sq2]
        Square.save_to_file(fsq)
        fsq2 = Square.load_from_file()
        self.assertNotEqual(fsq, fsq2)
