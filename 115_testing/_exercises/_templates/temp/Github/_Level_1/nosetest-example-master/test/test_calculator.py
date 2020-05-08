"""Tests For a simple Calculator App."""
import unittest
from app.calculator import Calculator


c_ TddPythonExample(unittest.TestCase):
    """The Test Class."""

    ___ setUp(self):
        """The setUp Method put things in place before each test case."""
        self.calc = Calculator()

    ___ test_calculator_add_method_returns_correct_result(self):
        """Test For Add Method."""
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    ___ test_calculator_returns_error_if_both_args_not_numbers(self):
        """Test that raises ValueError when Strings are passed in."""
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    ___ test_calculator_returns_error_message_if_x_arg_not_number(self):
        """Test that raises ValueError when x arg isn't a number."""
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    ___ test_calculator_returns_error_message_if_y_arg_not_number(self):
        """Test that raises ValueError when y arg isn't a number."""
        self.assertRaises(ValueError, self.calc.add, 2, 'three')


if __name__ == '__main__':
    unittest.main()
