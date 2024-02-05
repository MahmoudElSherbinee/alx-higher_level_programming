#!/usr/bin/python3
""" MyInt Class inherted from int """


class MyInt(int):
    """ Define the Myint class that is inherted from int """
    def __eq__(self, value):
        """ Change the proprety of the equal to operator

        Args:
          value: Other value to compare to.

        Return:
          True if they are not equal False if they are equal.
        """
        return (self.real != value)

    def __ne__(self, value):
        """ Change the proprety of the not equal to operator

        Args:
          value: Other value to compare to.

        Return:
          False if they are not equal True if they are equal.
        """
        return (self.real == value)
