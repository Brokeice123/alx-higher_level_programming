#!/usr/bin/python3
"""
The class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises an exception"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
