#!/usr/bin/python3
"""
Has the class Student
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
