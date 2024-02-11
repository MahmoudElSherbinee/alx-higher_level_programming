#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Define the Rectangle class that inhirite from the Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize instance of rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Width getter and setter
    @property
    def width(self):
        """ Get the width of a rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the width of a rectangle

        Args:
          value: Value to assign
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Height getter and setter
    @property
    def height(self):
        """ Get the height of a rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the height of a rectangle

        Args:
          value: Value to assign
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        """ Get the x of a rectangle """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Set the x of a rectangle

        Args:
          value: Value to assign
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        """ Get the y of a rectangle """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Set the y of a rectangle

        Args:
          value: Value to assign
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Public method area()
    def area(self):
        """ Return The area of the rectangle """
        return (self.width * self.height)

    # Public method display()
    def display(self):
        """ Print the rectangle to the stdout """
        char = '#'
        print("\n" * self.y, end="")
        print('\n'.join([" " * self.x + char * self.width] * self.height))

    # __str__ method
    def __str__(self):
        """ Return a string represntation of the object Rectangle """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    # Public methos update
    def update(self, *args, **kwargs):
        """ Update the rectangle

        *args:
          1st argument should be the id attribute
          2nd argument should be the width attribute
          3rd argument should be the height attribute
          4th argument should be the x attribute
          5th argument should be the y attribute

        **kwargs: key=value for each attribute
        """
        if args and len(args) > 0:
            if len(args) >= 1 and args[0] is not None:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id" and v is not None:
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    # Public method to_dictionary
    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle """
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
