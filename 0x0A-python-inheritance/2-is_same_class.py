#!/usr/bin/python3
""" Inhirtence modual """


def is_same_class(obj, a_class):
    """ Check if an object is an instance of a class

    Args:
      obj (object): Object to check.
      a_class: Class to check.

    Return:
      True if the object is instance of the class False otherwise
    """
    return (type(obj) == a_class)
