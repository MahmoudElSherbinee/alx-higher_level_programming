#!/usr/bin/python3
""" Inhirtence modual """


def inherits_from(obj, a_class):
    """ Check if an object is an instance of a class or subcalss

    Args:
      obj (object): Object to check.
      a_class: Class to check.

    Return:
      True if the object is instance of the class False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
