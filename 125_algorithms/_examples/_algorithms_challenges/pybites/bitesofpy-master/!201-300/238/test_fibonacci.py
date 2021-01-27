import pytest
from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
def test_fib_zero():
    a__ fib(0) == 0


def test_fib_neg():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_pos():
    a__ fib(1) == 1
    a__ fib(10) == 55
