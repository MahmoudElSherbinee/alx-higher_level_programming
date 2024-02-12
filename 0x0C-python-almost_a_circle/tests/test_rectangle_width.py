#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_width(unittest.TestCase):
    """ Test width getter and setter and type / value validation"""

    def test_private_attr_width(self):
        """ Test if width is private """
        r1 = Rectangle(4, 6)
        with self.assertRaises(AttributeError):
            print(r1.__width)

    def test_width_getter(self):
        """ Test the width getter """
        r1 = Rectangle(14, 10)
        self.assertEqual(r1.width, 14)

    def test_width_setter_str(self):
        """ Test passing width as string """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("hi", 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = "hi"

    def test_width_setter_list(self):
        """ Test passing width as list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle([1, 2], 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = [1, 2]

    def test_width_setter_set(self):
        """ Test passing width as list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({1, 2}, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = {1, 2}

    def test_width_setter_tuple(self):
        """ Test passing width as tuple """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle((1, 2), 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = (1, 2)

    def test_width_setter_bool(self):
        """ Test passing width as boolian """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(True, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = False

    def test_width_setter_dict(self):
        """ Test passing width as dictionary """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({"one": 1, "two": 2}, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = {"one": 1, "two": 2}

    def test_width_setter_float(self):
        """ Test passing width as dictionary """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(1.5, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = 1.5

    def test_width_setter_none(self):
        """ Test passing width as None """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(None, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = None

    def test_width_setter_complex(self):
        """ Test the setter for width with complex number """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(complex(5), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = complex(5)

    def test_width_setter_frozenset(self):
        """ Test the setter for width with frozenset """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(frozenset({1, 2, 3, 1}), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = frozenset({1, 2, 3, 1})

    def test_width_setter_range(self):
        """ Test the setter for width with range """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(range(5), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = range(5)

    def test_width_setter_bytes(self):
        """ Test the setter for width with bytes """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(b'Python', 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = b'Python'

    def test_width_setter_bytearray(self):
        """ Test the setter for width with bytearray """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(bytearray(b'abcdefg'), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = bytearray(b'abcdefg')

    def test_width_setter_memoryview(self):
        """ Test the setter for width with memoryview """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(memoryview(b'abcedfg'), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = memoryview(b'abcedfg')

    def test_width_setter_inf(self):
        """ Test the setter for width with inifinity """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(float('inf'), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = float('inf')

    def test_width_nan(self):
        """ Test the setter for width with nan """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(float('nan'), 2)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.width = float('nan')

    def test_width_setter_zero(self):
        """ Test passing width as zero """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.width = 0

    def test_width_setter_negative_value(self):
        """ Test passing width as negative value """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(-4, 10)

        r2 = Rectangle(10, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.width = -4
