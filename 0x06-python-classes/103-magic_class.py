#!/usr/bin/python3

""" Creating a magicclass"""

import math


class MagicClass:
    """the MagicClass"""

    def __init__(self, radius=0):
        """the data"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self._MagicClass__radius
