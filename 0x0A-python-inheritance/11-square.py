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

    def area(self):
        """ return the area of the square """
        return (self.__size ** 2)

    def __str__(self):
        """ Return  a string representation of the square """
        return ("[Square] {}/{}".format(self.__size, self.__size))
