#!/usr/bin/python3
"""
This is the add_integer module.
The add_integer module supplies one function, add_integer(a, b).
The function add_integer(a, b) returns the sum of a and b.
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
