from nose import with_setup

from unnecessary_math import multiply

def my_setup_function():
    pass


def my_teardown_function():
    pass


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    assert multiply(3, 4) == 12


test_numbers_3_4.setup = my_setup_function
test_numbers_3_4.teardown = my_teardown_function