#!/usr/bin/python3
""" Add Atrribute modual """


def add_attribute(obj, name, value):
    """ Add an atrubute to an object

    Args:
      obj (object): Object to add to.
      name: Name of the new attribute.
      value: Value of the new attribut.

    Raises:
      TypeError if the new attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
