"""

"""

import unittest

from my_module import utils

class UtilsTest(unittest.TestCase):

    def test_my_func(self):
        self.assertTrue(utils.MyFunction('aaa'))
        self.assertTrue(utils.MyFunction((1,2,3)))
        self.assertTrue(utils.MyFunction([1, 2, 3]))
        self.assertTrue(utils.MyFunction({1,2,3}))

        self.assertFalse(utils.MyFunction(42))
        self.assertFalse(utils.MyFunction(3.14))

