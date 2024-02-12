#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_y(unittest.TestCase):
    """ Test y getter and setter and type / value validation"""

    def test_private_attr_y(self):
        """ Test if y is private """
        r1 = Rectangle(4, 6)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_y_getter(self):
        """ Test the y getter """
        r1 = Rectangle(14, 10, 2, 2)
        self.assertEqual(r1.y, 2)

    def test_y_setter_str(self):
        """ Test passing y as string """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 10, 2, "hi")

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = "hi"

    def test_y_setter_list(self):
        """ Test passing y as list """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 10, 2, [1, 2])

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = [1, 2]

    def test_x_setter_set(self):
        """ Test passing y as list """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 5, 2, {1, 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = {1, 2}

    def test_x_setter_tuple(self):
        """ Test passing y as tuple """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 6, 2, (1, 2))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = (1, 2)

    def test_x_setter_bool(self):
        """ Test passing y as boolian """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 7, 2, True)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = False

    def test_x_setter_dict(self):
        """ Test passing y as dictionary """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 8, 2, {"one": 1, "two": 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = {"one": 1, "two": 2}

    def test_x_setter_float(self):
        """ Test passing y as dictionary """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 10, 2, 10.5)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = 1.5

    def test_x_setter_none(self):
        """ Test passing y as None """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 14, 2, None)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = None

    def test_x_setter_complex(self):
        """ Test the setter for y with complex number """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 6, 2, complex(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = complex(5)

    def test_x_setter_frozenset(self):
        """ Test the setter for y with frozenset """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 7, 2, frozenset({1, 2, 3, 1}))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = frozenset({1, 2, 3, 1})

    def test_x_setter_range(self):
        """ Test the setter for y with range """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 9, 2, range(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = range(5)

    def test_x_setter_bytes(self):
        """ Test the setter for y with bytes """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 10, 2, b'Python')

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = b'Python'

    def test_x_setter_bytearray(self):
        """ Test the setter for y with bytearray """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 3, 2, bytearray(b'abcdefg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = bytearray(b'abcdefg')

    def test_x_setter_memoryview(self):
        """ Test the setter for y with memoryview """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 4, 2, memoryview(b'abcedfg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = memoryview(b'abcedfg')

    def test_x_setter_inf(self):
        """ Test the setter for y with inifinity """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 5, 2, float('inf'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = float('inf')

    def test_x_nan(self):
        """ Test the setter for y with nan """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 8, 2, float('nan'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.y = float('nan')

    def test_x_setter_zero(self):
        """ Test passing y as zero """
        r1 = Rectangle(10, 10, 2, 0)
        self.assertEqual(r1.y, 0)

    def test_x_setter_negative_value(self):
        """ Test passing y as negative value """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(10, 10, 2, -5)

        r2 = Rectangle(10, 4, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.y = -4
