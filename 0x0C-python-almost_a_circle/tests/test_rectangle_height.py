#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_height(unittest.TestCase):
    """ Test height getter and setter and type / value validation"""

    def test_private_attr_height(self):
        """ Test if height is private """
        r1 = Rectangle(4, 6)
        with self.assertRaises(AttributeError):
            print(r1.__height)

    def test_height_getter(self):
        """ Test the height getter """
        r1 = Rectangle(14, 10)
        self.assertEqual(r1.height, 10)

    def test_height_setter_str(self):
        """ Test passing height as string """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, "hi")

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = "hi"

    def test_height_setter_list(self):
        """ Test passing height as list """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, [1, 2])

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = [1, 2]

    def test_height_setter_set(self):
        """ Test passing height as list """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, {1, 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = {1, 2}

    def test_height_setter_tuple(self):
        """ Test passing height as tuple """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, (1, 2))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = (1, 2)

    def test_height_setter_bool(self):
        """ Test passing height as boolian """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, True)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = False

    def test_height_setter_dict(self):
        """ Test passing height as dictionary """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, {"one": 1, "two": 2})

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = {"one": 1, "two": 2}

    def test_height_setter_float(self):
        """ Test passing height as dictionary """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, 10.5)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = 1.5

    def test_height_setter_none(self):
        """ Test passing height as None """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, None)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = None

    def test_height_setter_complex(self):
        """ Test the setter for height with complex number """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, complex(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = complex(5)

    def test_height_setter_frozenset(self):
        """ Test the setter for height with frozenset """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, frozenset({1, 2, 3, 1}))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = frozenset({1, 2, 3, 1})

    def test_height_setter_range(self):
        """ Test the setter for height with range """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, range(5))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = range(5)

    def test_height_setter_bytes(self):
        """ Test the setter for height with bytes """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, b'Python')

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = b'Python'

    def test_height_setter_bytearray(self):
        """ Test the setter for height with bytearray """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, bytearray(b'abcdefg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = bytearray(b'abcdefg')

    def test_height_setter_memoryview(self):
        """ Test the setter for height with memoryview """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, memoryview(b'abcedfg'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = memoryview(b'abcedfg')

    def test_height_setter_inf(self):
        """ Test the setter for height with inifinity """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, float('inf'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = float('inf')

    def test_height_nan(self):
        """ Test the setter for height with nan """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, float('nan'))

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = float('nan')

    def test_height_setter_zero(self):
        """ Test passing height as zero """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, 0)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = 0

    def test_height_setter_negative_value(self):
        """ Test passing height as negative value """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, -5)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = -4
