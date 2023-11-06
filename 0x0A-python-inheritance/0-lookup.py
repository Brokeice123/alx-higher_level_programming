#!/usr/bin/python3
"""
Contains a function that prints a list of available attributes and methods of an object
"""


def lookup(obj):
    """Prints a list of available attributes and methods of an object"""
    return dir(obj)
