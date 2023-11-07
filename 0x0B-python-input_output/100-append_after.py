#!/usr/bin/python3
"""
append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string at the end of a text file"""
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
