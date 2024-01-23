#!/usr/bin/python3
""" Creating a class called Square """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """size"""
        self.__size = size

    def __eq__(self, other):
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size to equal value"""
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square"""
        return self.__size ** 2
