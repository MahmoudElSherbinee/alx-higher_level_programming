#!/usr/bin/python3
""" Square class inherted from Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Define Square class dervided from Rectangle """
    def __init__(self, size):
        """ Initialize a new square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
