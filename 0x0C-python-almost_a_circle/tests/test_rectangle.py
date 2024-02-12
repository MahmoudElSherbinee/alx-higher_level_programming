#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Initialisation(unittest.TestCase):
    """ Test the initialisation of the object Rectangle """

    def test_rectangle_instance_of_Base(self):
        """ Test if Rectangle is instance of Base"""
        r1 = Rectangle(10, 15)
        self.assertIsInstance(r1, Base)

    def test_wrong_number_of_arguments(self):
        """
        test the case of wrong number of arguments
        number of arguments should be btween 2 and 5
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

        with self.assertRaises(TypeError):
            r2 = Rectangle(12)

        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 15, 2, 2, 10, 15)

    def test_correct_number_of_arguments(self):
        """ Test the case of correct number of argument arguments """
        r1 = Rectangle(10, 15)
        r2 = Rectangle(15, 20, 2)
        r3 = Rectangle(15, 20, 2, 3)
        r4 = Rectangle(15, 20, 2, 3, 14)
