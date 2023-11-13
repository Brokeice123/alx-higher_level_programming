#!/usr/bin/python3
"""Unittest for rectangle.py
Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_area
    TestRectangle_stdout
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_dict
"""
import unittest
import io
import sys
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


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__  and display methods of Rectangle class"""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures the output of a method and returns it as a string"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__
    def test_rectangle_str(self):
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 10/2", str(r))

    def test_str_changed_values(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.width = 1
        r.height = 2
        self.assertEqual("[Rectangle] (50) 30/40 - 1/2", str(r))

    # Test display
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", catch.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", catch.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, catch.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        catch = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, catch.getvalue())


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args of Rectangle class"""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, 3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, 3, 4)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(1, "2")

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(1, 2, "3")

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(1, 2, 3, "4")

    def test_update_args_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(1, 2, 3, 4, "5")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs of Rectangle class"""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3, x=4)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r.update(id=1, width="2")

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r.update(id=1, height="2")

    def test_update_kwargs_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r.update(id=1, x="2")

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r.update(id=1, y="2")


class TestRectangle_dict(unittest.TestCase):
    """Unittests for testing to_dictionary method of Rectangle class"""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
