# only be executed with option --all-module

from nose.tools import raises, timed, istest, nottest
import time


@raises(TypeError, ValueError)
def test_raises_type_error():
    raise TypeError("This test passes")

@timed(.3)
def test_timed():
    time.sleep(.2)

@istest
def this_is_a_test():
    pass

# note this test won't pass if you use py.test
@nottest
def test_this_is_not_a_test():
    assert False

def test_how_debug_works():
    assert False
