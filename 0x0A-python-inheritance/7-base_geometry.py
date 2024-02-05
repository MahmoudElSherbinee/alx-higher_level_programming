#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ Define a BaseGeometry class """

    def area(self):
        """ Raise an exception with the area not emplimented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate the value

        Args:
          name (str): Name of the value.
          value (int): Value to validate.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
