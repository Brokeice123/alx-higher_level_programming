#!/usr/bin/python3
"""Unittest for base.py
Unittest classes:
    TestBase_instantiation
    TestBase_to_json_string
"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Unittest to test instantiation in base.py"""

    def test_no_args(self):
        b1 = Base()
        self.assertNotEqual(b1.id, 1)

    def test_with_id(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_with_id2(self):
        b3 = Base()
        self.assertNotEqual(b3.id, 2)

    def test_with_id3(self):
        b4 = Base()
        self.assertNotEqual(b4.id, 3)

    def test_with_id4(self):
        b5 = Base()
        self.assertNotEqual(b5.id, 4)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertNotEqual(b1.id, b2.id)

    def test_nd_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_objects)

    def test_float_id(self):
        b1 = Base(1.5)
        self.assertEqual(b1.id, 1.5)

    def test_str_id(self):
        b1 = Base("string")
        self.assertEqual(b1.id, "string")

    def test_bool_id(self):
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_list_id(self):
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_dict_id(self):
        b1 = Base({"key": "value"})
        self.assertEqual(b1.id, {"key": "value"})


class TestBase_to_json_string(unittest.TestCase):
    """Unittest to test to_json_string in base.py"""

    def test_to_json_string_list(self):
        list_dictionaries = [{"key": "value"}, {"key": "value2"}]
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[{"key": "value"}, {"key": "value2"}]')

    def test_to_json_string_dict(self):
        dictionary = {"key": "value"}
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '{"key": "value"}')

    def test_to_json_string_empty_list(self):
        list_dictionaries = []
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_string_empty_dict(self):
        dictionary = {}
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_string_None(self):
        list_dictionaries = None
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_dictionary, '[]')


if __name__ == "__main__":
    unittest.main()
