#!/usr/bin/python3
"""
A module that contains a function that writes an object to a text file
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(my_obj)
