#!/usr/bin/python3
"""
A module that contains a function that writes an object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
