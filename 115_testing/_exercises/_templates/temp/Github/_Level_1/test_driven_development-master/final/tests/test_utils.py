"""

"""

______ u__
______ mock

____ my_module ______ utils

c_ UtilsTest?.?

    ___ test_my_func
        aT..(utils.MyFunction('aaa'))
        aT..(utils.MyFunction((1,2,3)))
        aT..(utils.MyFunction([1, 2, 3]))
        aT..(utils.MyFunction({1,2,3}))

        assertFalse(utils.MyFunction(42))
        assertFalse(utils.MyFunction(3.14))

    @mock.patch("my_module.utils.sleep", return_value _ None)
    ___ test_my_long_func  mocked_sleep
        assertEquals('AAA', utils.MyLongFunction('aaa', 5))
        
