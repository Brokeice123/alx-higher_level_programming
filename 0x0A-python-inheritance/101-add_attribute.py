#!/usr/bin/python3
"""
Adds a new attribute to an object if it's possible
"""


def add_attribute(obj, key, value):
    """Adds a new attribute to an object if it's possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
