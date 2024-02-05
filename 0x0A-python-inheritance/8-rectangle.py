#!/usr/bin/python3
""" Rectangle class inherted from BaseGeometry """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Define Rectangle class dervided from BaseGeometry """

    def __init__(self, width, height):
        """ Initialize a new rectangle

        Args:
          width (integer): Width of the rectangle.
          height (integer): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
