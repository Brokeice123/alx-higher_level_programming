#!/usr/bin/python3
"""Unittest for square.py
Unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare_instantiation(unittest.TestCase):
    """Unittest for Square instantiation"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(2, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 3)
        s2 = Square(2, 2, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(2, 2, 3, 4)
        self.assertEqual(s1.id, s2.id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_size_setter(self):
        s1 = Square(1, 2, 3, 4)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_size_getter(self):
        s1 = Square(1, 2, 3, 4)
        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_width_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.width, 1)

    def test_height_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.height, 1)

    def test_x_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.x, 2)

    def test_y_getter(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.y, 3)


class TestSquare_size(unittest.TestCase):
    """Unittest for Square size"""

    def test_None_size(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_float_size(self):
        with self.assertRaises(TypeError):
            Square(1.1)

    def test_list_size(self):
        with self.assertRaises(TypeError):
            Square([1])

    def test_tuple_size(self):
        with self.assertRaises(TypeError):
            Square((1,))

    def test_set_size(self):
        with self.assertRaises(TypeError):
            Square({1})

    def test_dict_size(self):
        with self.assertRaises(TypeError):
            Square({"a": 1})

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittest for Square x"""

    def test_None_x(self):
        with self.assertRaises(TypeError):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaises(TypeError):
            Square(1, "1")

    def test_float_x(self):
        with self.assertRaises(TypeError):
            Square(1, 1.1)

    def test_list_x(self):
        with self.assertRaises(TypeError):
            Square(1, [1])

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            Square(1, (1,))

    def test_set_x(self):
        with self.assertRaises(TypeError):
            Square(1, {1})

    def test_dict_x(self):
        with self.assertRaises(TypeError):
            Square(1, {"a": 1})

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -1)


class TestSquare_y(unittest.TestCase):
    """Unittest for Square y"""

    def test_None_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "1")

    def test_float_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 1.1)

    def test_list_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, [1])

    def test_tuple_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, (1,))

    def test_set_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, {1})

    def test_dict_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, {"a": 1})

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -1)


if __name__ == "__main__":
    unittest.main()
