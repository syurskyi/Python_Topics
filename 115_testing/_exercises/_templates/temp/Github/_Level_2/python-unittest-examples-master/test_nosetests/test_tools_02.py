from nose.tools import raises, timed, istest, nottest
import time


@raises(TypeError, ValueError)
___ test_raises_type_error():
    raise TypeError("This test passes")

@timed(.3)
___ test_timed():
    time.sleep(.2)

@istest
___ this_is_a_test():
    pass

# note this test won't pass if you use py.test
@nottest
___ test_this_is_not_a_test():
    assert False
