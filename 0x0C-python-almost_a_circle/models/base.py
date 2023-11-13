#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary (dict): Key/value pairs to set into the new instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances with all attributes already set
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances with all attributes already set
        """
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                               for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
