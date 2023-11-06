#!/usr/bin/python3
"""
Defines a class MyList.
"""


class MyList(list):
    """A class that inherits from list"""
    def __init__(self):
        """Instantiation"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
