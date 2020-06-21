import unittest
from src.exampleCode1 import MyClass1


class TestMyClass1(unittest.TestCase):

    def test_constructor1(self):
        obj = MyClass1()
        self.assertEqual(obj.a, 0)
        self.assertEqual(obj.b, 1)
        self.assertEqual(obj.c, 2)

    def test_constructor2(self):
        obj = MyClass1(b=4.5, c=8)
        self.assertEqual(obj.a, 0)
        self.assertEqual(obj.b, 4.5)
        self.assertEqual(obj.c, 8)

    def test_product1(self):
        obj = MyClass1(1, 2, 3)
        self.assertEqual(obj.getProduct(), 6)

    def test_min1(self):
        obj = MyClass1(2, 2, 2)
        self.assertEqual(obj.getMin(), 2)

    def test_min2(self):
        obj = MyClass1(-10, 2, 3)
        self.assertEqual(obj.getMin(), -10)

    def test_max1(self):
        obj = MyClass1(1, 2, 3)
        self.assertEqual(obj.getMax(), 3)

    def test_sum1(self):
        obj = MyClass1(-1, 1, 0)
        self.assertEqual(obj.getSum(), 0)

    def test_sum2(self):
        obj = MyClass1(10, 20, 30)
        self.assertEqual(obj.getSum(), 60)

    def test_mean1(self):
        obj = MyClass1(10, 10, 10)
        self.assertEqual(obj.getMean(), 10)


if __name__ == '__main__':
    unittest.main()
