#!/usr/bin/python3
"""Text indentation module."""


def text_indentation(text):
    """Print text with 2 new lines after each of these characters: ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print(text)
