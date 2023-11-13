#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square
        Args:
            size (int): The size of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                    self.width)
