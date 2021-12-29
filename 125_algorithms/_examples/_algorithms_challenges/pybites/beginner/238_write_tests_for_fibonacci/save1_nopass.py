from fibonacci import fib
import pytest


def test_fib_main(n):
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(20) == 6765


def test_fib_negative(n):
    with pytest.raises(ValueError):
        fib(-1)


