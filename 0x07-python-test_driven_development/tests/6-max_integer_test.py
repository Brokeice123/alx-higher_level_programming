#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unitest class for max_integer function"""
    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_function_docstring(self):
        """Test for function docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test for list with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer(self):
        """Test for max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_list(self):
        """Test for negative list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_list(self):
        """Test for float list"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_string_list(self):
        """Test for string list"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_mixed_list(self):
        """Test for mixed list"""
        f = [1, 2.2, "Hello", 3]
        with self.assertRaises(TypeError):
            max_integer(f)

    def test_none(self):
        """Test for None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_string(self):
        """Test for empty string"""
        self.assertEqual(max_integer(""), None)

    def test_boolean(self):
        """Test for boolean"""
        with self.assertRaises(TypeError):
            max_integer(True)

if __name__ == '__main__':
    unittest.main()
