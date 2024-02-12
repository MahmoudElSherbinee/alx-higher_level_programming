#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_x(unittest.TestCase):
    """ Test x getter and setter and type / value validation"""

    def test_private_attr_x(self):
        """ Test if x is private """
        r1 = Rectangle(4, 6)
        with self.assertRaises(AttributeError):
            print(r1.__x)

    def test_x_getter(self):
        """ Test the x getter """
        r1 = Rectangle(14, 10, 2)
        self.assertEqual(r1.x, 2)

    def test_x_setter_str(self):
        """ Test passing x as string """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 10, "hi")

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = "hi"

    def test_x_setter_list(self):
        """ Test passing x as list """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 10, [1, 2])

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = [1, 2]

    def test_x_setter_set(self):
        """ Test passing x as list """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 5, {1, 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = {1, 2}

    def test_x_setter_tuple(self):
        """ Test passing x as tuple """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 6, (1, 2))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = (1, 2)

    def test_x_setter_bool(self):
        """ Test passing x as boolian """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 7, True)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = False

    def test_x_setter_dict(self):
        """ Test passing x as dictionary """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 8, {"one": 1, "two": 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = {"one": 1, "two": 2}

    def test_x_setter_float(self):
        """ Test passing x as dictionary """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 10, 10.5)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = 1.5

    def test_x_setter_none(self):
        """ Test passing x as None """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 14, None)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = None

    def test_x_setter_complex(self):
        """ Test the setter for x with complex number """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 6, complex(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = complex(5)

    def test_x_setter_frozenset(self):
        """ Test the setter for x with frozenset """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 7, frozenset({1, 2, 3, 1}))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = frozenset({1, 2, 3, 1})

    def test_x_setter_range(self):
        """ Test the setter for x with range """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 9, range(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = range(5)

    def test_x_setter_bytes(self):
        """ Test the setter for x with bytes """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 10, b'Python')

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = b'Python'

    def test_x_setter_bytearray(self):
        """ Test the setter for x with bytearray """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, bytearray(b'abcdefg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = bytearray(b'abcdefg')

    def test_x_setter_memoryview(self):
        """ Test the setter for x with memoryview """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 4, memoryview(b'abcedfg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = memoryview(b'abcedfg')

    def test_x_setter_inf(self):
        """ Test the setter for x with inifinity """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 5, float('inf'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = float('inf')

    def test_x_nan(self):
        """ Test the setter for x with nan """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 8, float('nan'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.x = float('nan')

    def test_x_setter_zero(self):
        """ Test passing x as zero """
        r1 = Rectangle(10, 10, 0)
        self.assertEqual(r1.x, 0)

    def test_x_setter_negative_value(self):
        """ Test passing x as negative value """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(10, 10, -5)

        r2 = Rectangle(10, 4, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.x = -4
