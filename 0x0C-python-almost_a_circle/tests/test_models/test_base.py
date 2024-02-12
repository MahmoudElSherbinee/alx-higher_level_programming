#!/usr/bin/python3
"""Usitest for the Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base Class """

    def test_instace_creation_with_id(self):
        """ Test instance creation with id """
        b = Base(41)
        self.assertEqual(b.id, 41)

    def test_instance_creation_without_id(self):
        """ Test instance creation without id """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_public_attr_id(self):
        """ Test the public attribute is """
        b1 = Base()
        b1.id = 7
        self.assertEqual(b1.id, 7)

    def test_creating_bases_with_and_without_id(self):
        """ Test creating multiple bases with id and without it """
        b1 = Base()
        b2 = Base(7)
        b3 = Base()
        b4 = Base()
        b4.id = 14
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 7)
        self.assertEqual(b4.id, 14)

    def test_private_attr_n_instance(self):
        """ test the private attribute __n_instances """
        with self.assertRaises(AttributeError):
            print(Base(7).__nb_instances)


if __name__ == "__main__":
    unittest.main()
