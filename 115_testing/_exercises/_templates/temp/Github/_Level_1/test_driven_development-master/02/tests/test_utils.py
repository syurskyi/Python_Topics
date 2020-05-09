"""

"""

______ unittest

____ my_module ______ utils

c_ UtilsTest(unittest.TestCase):

    ___ test_my_func
        assertTrue(utils.MyFunction('aaa'))
        assertTrue(utils.MyFunction((1,2,3)))
        assertTrue(utils.MyFunction([1, 2, 3]))
        assertTrue(utils.MyFunction({1,2,3}))

        assertFalse(utils.MyFunction(42))
        assertFalse(utils.MyFunction(3.14))

