#!/usr/bin/python3
"""
returns the JSON representation of an object
"""


def from_json_string(my_str):
    """returns the JSON representation of an object"""
    import json
    return json.loads(my_str)
