#!/usr/bin/python3
"""Unittest for rectangle.py
Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_area
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of Rectangle class"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 20)
        r2 = Rectangle(2, 10, 20)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(10, 2, 20, 30)
        r2 = Rectangle(2, 10, 20, 30)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        r2 = Rectangle(2, 10, 20, 30, 40)
        self.assertEqual(r1.id, r2.id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 20, 30, 40, 50)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 20, 30, 40).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 20, 30, 40).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 20, 30, 40).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 20, 30, 40).__y)

    def test_width_getter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        self.assertEqual(r1.width, 10)

    def test_height_getter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        self.assertEqual(r1.height, 2)

    def test_x_getter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        self.assertEqual(r1.x, 20)

    def test_y_getter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        self.assertEqual(r1.y, 30)

    def test_width_setter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        r1.width = 15
        self.assertEqual(r1.width, 15)

    def test_height_setter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        r1.height = 15
        self.assertEqual(r1.height, 15)

    def test_x_setter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        r1.x = 15
        self.assertEqual(r1.x, 15)

    def test_y_setter(self):
        r1 = Rectangle(10, 2, 20, 30, 40)
        r1.y = 15
        self.assertEqual(r1.y, 15)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing width attribute of Rectangle class"""

    def test_None_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("string", 2)

    def test_float_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(1.5, 2)

    def test_complex_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(complex(1, 2), 2)

    def test_list_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_dict_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(True, 2)

    def test_NaN_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(float("nan"), 2)

    def test_negative_width(self):
        with self.assertRaises(ValueError, msg="width must be >= 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaises(ValueError, msg="width must be >= 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing height attribute of Rectangle class"""

    def test_None_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "string")

    def test_float_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, 1.5)

    def test_complex_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, complex(1, 2))

    def test_list_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_dict_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_bool_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, True)

    def test_NaN_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, float("nan"))

    def test_negative_height(self):
        with self.assertRaises(ValueError, msg="height must be >= 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaises(ValueError, msg="height must be >= 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing x attribute of Rectangle class"""

    def test_None_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, "string")

    def test_float_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 1.5)

    def test_complex_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, complex(1, 2))

    def test_list_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])

    def test_dict_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2})

    def test_bool_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, True)

    def test_NaN_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, float("nan"))

    def test_negative_x(self):
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 2, -1)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing y attribute of Rectangle class"""

    def test_None_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, "string")

    def test_float_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, 1.5)

    def test_complex_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, complex(1, 2))

    def test_list_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, [1, 2, 3])

    def test_dict_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, {"a": 1, "b": 2})

    def test_bool_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, True)

    def test_NaN_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, float("nan"))

    def test_negative_y(self):
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 2, 3, -1)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing area attribute of Rectangle class"""

    def test_area_singledigit(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.area(), 2)

    def test_area_doubledigit(self):
        r = Rectangle(10, 20, 3, 4, 5)
        self.assertEqual(r.area(), 200)

    def test_area_multidigit(self):
        r = Rectangle(1000, 20, 3, 4, 5)
        self.assertEqual(r.area(), 20000)

    def test_area_changed_values(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.width = 1
        r.height = 2
        self.assertEqual(r.area(), 2)


if __name__ == "__main__":
    unittest.main()
