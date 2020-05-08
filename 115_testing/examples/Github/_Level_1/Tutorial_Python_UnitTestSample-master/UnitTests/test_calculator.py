import unittest
from Modules.Calculator.main import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Calculator()

    def test_add(self):
        expected = 5
        result = self.app.add(3,2)
        self.assertEqual(result,expected)

    def test_subtract(self):
        expected = 5
        result = self.app.subtract(10,5)
        self.assertEqual(result,expected)

    def test_multiply(self):
        expected = 5
        result = self.app.multiply(5,1)
        self.assertEqual(result,expected)

    def test_divide(self):
        expected = 5
        result = self.app.divide(10,2)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
