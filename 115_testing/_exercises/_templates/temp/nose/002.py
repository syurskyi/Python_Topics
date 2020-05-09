____ nose ______ with_setup

____ unnecessary_math ______ multiply

___ my_setup_function(
    pass


___ my_teardown_function(
    pass


@with_setup(my_setup_function, my_teardown_function)
___ test_numbers_3_4(
    assert multiply(3, 4) == 12


test_numbers_3_4.setup _ my_setup_function
test_numbers_3_4.teardown _ my_teardown_function