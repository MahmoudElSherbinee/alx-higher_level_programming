#!/usr/bin/python3
""" Unitest for class Rectangle """
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_area(unittest.TestCase):
    """ Test the public method area() """

    def test_area_with_argumen(self):
        """ Test area public method by passing an argument to it """
        r1 = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            r1.area(1)

    def test_area_valid(self):
        """ test a valid case of are """
        r1 = Rectangle(10, 4)
        self.assertEqual(r1.area(), 40)

    def test_area_larg_number(self):
        """ test a valid case of are """
        r1 = Rectangle(999999999999999, 9999999999999999)
        self.assertEqual(r1.area(), 9999999999999989000000000000001)

    def test_area_changed_attr(self):
        """ Test area after changing attributes """
        r1 = Rectangle(10, 4)
        r1.width = 15
        r1.height = 3
        self.assertEqual(r1.area(), 45)


class TestRectangle_diplay(unittest.TestCase):
    """ test the public method display """

    def test_display_with_arg(self):
        """ Test the public method display with an argument """
        r1 = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            r1.display(1)

    def test_diplay(self):
        """ Test the public method diplay """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(4, 5)
            r1.display()

            captured_output = mock_stdout.getvalue()
            self.assertEqual(captured_output, "####\n####\n####\n####\n####\n")

    def test_diplay_with_x(self):
        """ Test the public method diplay with x """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(3, 4, 2)
            r1.display()

            captured_output = mock_stdout.getvalue()
            self.assertEqual(captured_output, "  ###\n  ###\n  ###\n  ###\n")

    def test_diplay_with_y(self):
        """ Test the public method diplay with y """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(4, 4, 0, 3)
            r1.display()

            captured_output = mock_stdout.getvalue()
            self.assertEqual(captured_output, "\n\n\n####\n####\n####\n####\n")

    def test_diplay_with_x_y(self):
        """ Test the public method diplay with x and y """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(2, 4, 2, 3)
            r1.display()

            captured_output = mock_stdout.getvalue()
            self.assertEqual(captured_output, "\n\n\n  ##\n  ##\n  ##\n  ##\n")


class TestRectangle_str(unittest.TestCase):
    """ Test the str method of Rectangle """

    def test_str(self):
        """ test the return of str on Rectangle """
        r1 = Rectangle(10, 5, 0, 0, 79)
        self.assertEqual(str(r1), "[Rectangle] (79) 0/0 - 10/5")

    def test_str_with_x(self):
        """ test the return of str on Rectangle with x"""
        r1 = Rectangle(10, 5, 2, 0, 79)
        self.assertEqual(str(r1), "[Rectangle] (79) 2/0 - 10/5")

    def test_str_with_y(self):
        """ test the return of str on Rectangle with y """
        r1 = Rectangle(10, 5, 0, 2, 79)
        self.assertEqual(str(r1), "[Rectangle] (79) 0/2 - 10/5")

    def test_str_with_x_y(self):
        """ test the return of str on Rectangle with x and y"""
        r1 = Rectangle(10, 5, 2, 3, 79)
        self.assertEqual(str(r1), "[Rectangle] (79) 2/3 - 10/5")


class TestRectangle_update_args(unittest.TestCase):
    """ Test the update method for Rectangle """

    def test_update_args_no_aruments(self):
        """ Test the update methos with no arguments """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r1))

    def test_update_args_one_aruments(self):
        """ Test the update methos with one argument id """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(47)
        self.assertEqual("[Rectangle] (47) 10/10 - 10/10", str(r1))

    def test_update_args_two_aruments(self):
        """ Test the update methos with two arguments, id and width """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(49, 7)
        self.assertEqual("[Rectangle] (49) 10/10 - 7/10", str(r1))

    def test_update_args_three_aruments(self):
        """
        Test the update methos with three arguments, id, width and height
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(11, 7, 3)
        self.assertEqual("[Rectangle] (11) 10/10 - 7/3", str(r1))

    def test_update_args_four_aruments(self):
        """
        Test the update methos with four arguments, id, width, height, and x
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(9, 5, 2, 3)
        self.assertEqual("[Rectangle] (9) 3/10 - 5/2", str(r1))

    def test_update_args_five_aruments(self):
        """
        Test the update methos with four arguments, id, width, height, x and y
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(9, 5, 2, 3, 7)
        self.assertEqual("[Rectangle] (9) 3/7 - 5/2", str(r1))

    def test_update_args_more_than_five_aruments(self):
        """
        Test the update methos with more than five arguments, id, width,
        height, and x, plus other arguments
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(9, 5, 2, 3, 1, 54, 66)
        self.assertEqual("[Rectangle] (9) 3/1 - 5/2", str(r1))

    def test_update_args_with_id_is_none(self):
        """
        Test the update methos for all arguments, id = None, width, height, x
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(None, 5, 2, 3, 5)
        self.assertEqual("[Rectangle] (10) 3/5 - 5/2", str(r1))


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
