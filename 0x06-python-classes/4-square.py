#!/usr/bin/python3
""" Creating a class called Square """


class Square:
    """ Define a private instance attr size """

    def __init__(self, size=0):
        """ Initialize size attribute. """
        self.__size = size
        """ creating the size attr """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
