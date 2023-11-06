#!/usr/bin/python3
"""
A class that inherits from int
"""


class MyInt(int):
    """
    A class that inherits from int
    """

    def __eq__(self, other):
        """
        Returns True if self is equal to other
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Returns True if self is not equal to other
        """
        return not super().__ne__(other)
