# test_calculator.py
import unittest
from app.calculator import Calculator


c_ TddInPythonExample(unittest.TestCase):
    """docstring for TddInPythonExample"""

    ___ setUp(self):
        self.calc = Calculator()

    ___ test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    ___ test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    ___ test_calculator_returns_error_message_if_x_args_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    ___ test_calculator_returns_error_message_if_y_args_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')


if __name__ == '__main__':
    unittest.main()
