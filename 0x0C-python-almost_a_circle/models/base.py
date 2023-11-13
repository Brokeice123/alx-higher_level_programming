#!/usr/bin/python3
"""Defines a base model class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string (str): A JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
