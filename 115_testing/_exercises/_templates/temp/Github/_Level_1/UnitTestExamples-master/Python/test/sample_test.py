import sys
import unittest

from sample import Calc


c_ TestSample(unittest.TestCase):
    @classmethod
    ___ setUpClass(cls):
        cls.calc = Calc()

    ___ test_add(self):
        self.assertEqual(15, self.calc.add(10, 5))
        self.assertEqual(5, self.calc.add(8, -3))

    ___ test_pow(self):
        self.assertEqual(125, self.calc.pow(5, 3))
        self.assertEqual(sys.maxsize, self.calc.pow(2, 31) - 1)


___ suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
