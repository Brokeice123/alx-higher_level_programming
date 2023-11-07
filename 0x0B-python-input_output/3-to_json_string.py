#!/usr/bin/python3
"""
Module that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    import json
    return json.dumps(my_obj)
