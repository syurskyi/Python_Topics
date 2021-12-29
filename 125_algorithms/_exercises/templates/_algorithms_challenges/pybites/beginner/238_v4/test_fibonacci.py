import pytest
from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
___ test_fib_zero():
    assert fib(0) == 0


___ test_fib_neg():
    with pytest.raises(ValueError):
        fib(-1)


___ test_fib_pos():
    assert fib(1) == 1
    assert fib(10) == 55
