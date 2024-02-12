#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Id(unittest.TestCase):
    """ Test the id of Rectangle """

    def test_init_without_id(self):
        """ Test initializing a Rectangle without the id atribute """
        r1 = Rectangle(10, 15)

    def test_init_with_id(self):
        """ Test initializing with id """
        r1 = Rectangle(15, 20, 1, 1, 17)
        self.assertEqual(r1.id, 17)

    def test_multi_id(self):
        """ Test the id of multiple Rectangles """
        r1 = Rectangle(10, 15)
        r2 = Rectangle(4, 25)
        r3 = Rectangle(4, 25, 2, 2, 17)
        r4 = Rectangle(6, 5)

        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, 17)
        self.assertEqual(r4.id, r1.id + 2)

    def test_public_attr_id(self):
        """ Test the public attribute id """
        r1 = Rectangle(4, 2)
        r1.id = 14
        self.assertEqual(r1.id, 14)
