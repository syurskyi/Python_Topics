____ n__.tools ______ with_setup
____ n__.plugins.deprecated ______ DeprecatedTest
____ n__.plugins.skip ______ SkipTest
____ n__.tools ______ nottest


global_a, global_b _ 0, 0


___ setup_func(
    global global_a, global_b
    global_a, global_b _ 1, 1


___ teardown_func(
    p..

# note that with_setup is useful only for test functions, not for test methods
# in unittest.TestCase subclasses or other test classes.


@with_setup(setup_func, teardown_func)
___ test_fixture(
    a.. global_a + global_b __ 2

#--------------------------------------
# nose supports test functions and methods that are generators.
# the following test case will generate five test results


___ test_evens(
    ___ i __ ra..(0, 5
        yield check_even, i


# We can put with_setup on the method test_events, then the setup and teardown
# functions will only be executed once. If we instead put the functions on the
# method check_even, then setup and teardown functions will be executed five
# times.
___ check_even(n
    a.. n < 5


___ test_basic_assertion(
    a.. (1,2,3) __ (1,2,3)
    a.. [1,2,3] __ [1,2,3]
    a.. {'key1': 1, 'key2': 2} __ {'key1': 1, 'key2': 2}

___ test_deprecated_test_case(
    r_ DeprecatedTest

___ test_skip_plugin(
    r_ SkipTest


@nottest
___ test_not_a_test(
    p..
