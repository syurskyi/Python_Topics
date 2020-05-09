____ nose.tools ______ with_setup
____ nose.plugins.deprecated ______ DeprecatedTest
____ nose.plugins.skip ______ SkipTest
____ nose.tools ______ nottest


global_a, global_b _ 0, 0


___ setup_func(
    global global_a, global_b
    global_a, global_b _ 1, 1


___ teardown_func(
    pass

# note that with_setup is useful only for test functions, not for test methods
# in unittest.TestCase subclasses or other test classes.


@with_setup(setup_func, teardown_func)
___ test_fixture(
    assert global_a + global_b == 2

#--------------------------------------
# nose supports test functions and methods that are generators.
# the following test case will generate five test results


___ test_evens(
    for i in range(0, 5
        yield check_even, i


# We can put with_setup on the method test_events, then the setup and teardown
# functions will only be executed once. If we instead put the functions on the
# method check_even, then setup and teardown functions will be executed five
# times.
___ check_even(n
    assert n < 5


___ test_basic_assertion(
    assert (1,2,3) == (1,2,3)
    assert [1,2,3] == [1,2,3]
    assert {'key1': 1, 'key2': 2} == {'key1': 1, 'key2': 2}

___ test_deprecated_test_case(
    raise DeprecatedTest

___ test_skip_plugin(
    raise SkipTest


@nottest
___ test_not_a_test(
    pass
