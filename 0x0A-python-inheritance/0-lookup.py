#!/usr/bin/python3
""" Lookup modual """


def lookup(object):
    """ returns the list of available attributes and methods of an object

    Args:
      object (object): The object to return it attributes and methodes
    """
    return (dir(object))
