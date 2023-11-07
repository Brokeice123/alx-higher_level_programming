#!/usr/bin/python3
"""
append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string at the end of a text file"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        content = f.read()
        content = content.replace(search_string, new_string)
        f.seek(0)
        f.write(content)
