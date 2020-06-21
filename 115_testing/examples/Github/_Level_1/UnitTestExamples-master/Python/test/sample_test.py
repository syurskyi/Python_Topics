import sys
import unittest

from sample import Calc


class TestSample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = Calc()

    def test_add(self):
        self.assertEqual(15, self.calc.add(10, 5))
        self.assertEqual(5, self.calc.add(8, -3))

    def test_pow(self):
        self.assertEqual(125, self.calc.pow(5, 3))
        self.assertEqual(sys.maxsize, self.calc.pow(2, 31) - 1)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
