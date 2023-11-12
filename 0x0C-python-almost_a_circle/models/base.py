#!/usr/bin/python3
"""Defines a base model class"""


class Base:
    """Represent the base model
    Represents the base for all other classes in the project
    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id (int): The identity of the Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
