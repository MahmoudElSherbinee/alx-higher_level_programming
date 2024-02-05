#!/usr/bin/python3
""" Define a Class MyList """


class MyList(list):
    """ Mylist class derived from list """

    def print_sorted(self):
        """ Pritn the list sorted """
        print(sorted(self))
