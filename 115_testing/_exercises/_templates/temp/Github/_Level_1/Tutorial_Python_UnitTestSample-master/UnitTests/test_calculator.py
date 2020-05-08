import unittest
from Modules.Calculator.main import Calculator


c_ MyTestCase(unittest.TestCase):

    ___ setUp(self):
        self.app = Calculator()

    ___ test_add(self):
        expected = 5
        result = self.app.add(3,2)
        self.assertEqual(result,expected)

    ___ test_subtract(self):
        expected = 5
        result = self.app.subtract(10,5)
        self.assertEqual(result,expected)

    ___ test_multiply(self):
        expected = 5
        result = self.app.multiply(5,1)
        self.assertEqual(result,expected)

    ___ test_divide(self):
        expected = 5
        result = self.app.divide(10,2)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
