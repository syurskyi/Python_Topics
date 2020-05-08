"""

"""

import unittest

from my_module import utils

c_ UtilsTest(unittest.TestCase):

    ___ test_my_func(self):
        self.assertTrue(utils.MyFunction('aaa'))
        self.assertTrue(utils.MyFunction((1,2,3)))
        self.assertTrue(utils.MyFunction([1, 2, 3]))
        self.assertTrue(utils.MyFunction({1,2,3}))

        self.assertFalse(utils.MyFunction(42))
        self.assertFalse(utils.MyFunction(3.14))

    ___ test_my_long_func(self):
        self.assertEquals('AAA', utils.MyLongFunction('aaa', 5))
