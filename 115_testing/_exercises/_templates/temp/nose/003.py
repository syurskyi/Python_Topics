____ nose ______ with_setup  # optional

____ unnecessary_math ______ multiply


___ setup_module(module
    print("")  # this is to get a newline after the dots
    print("setup_module before anything in this file")


___ teardown_module(module
    print("teardown_module after everything in this file")


___ my_setup_function(
    print("my_setup_function")


___ my_teardown_function(
    print("my_teardown_function")


@with_setup(my_setup_function, my_teardown_function)
___ test_numbers_3_4(
    print('test_numbers_3_4  <============================ actual test code')
    assert multiply(3, 4) == 12


@with_setup(my_setup_function, my_teardown_function)
___ test_strings_a_3(
    print('test_strings_a_3  <============================ actual test code')
    assert multiply('a', 3) == 'aaa'


c_ TestUM:

    ___ setup
        print("TestUM:setup() before each test method")

    ___ teardown
        print("TestUM:teardown() after each test method")

    @classmethod
    ___ setup_class(cls
        print("setup_class() before any methods in this class")

    @classmethod
    ___ teardown_class(cls
        print("teardown_class() after any methods in this class")

    ___ test_numbers_5_6
        print
        'test_numbers_5_6()  <============================ actual test code'
        assert multiply(5, 6) == 30

    ___ test_strings_b_2
        print
        'test_strings_b_2()  <============================ actual test code'
        assert multiply('b', 2) == 'bb'