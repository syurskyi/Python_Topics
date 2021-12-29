from fibonacci import fib
import pytest


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8


def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-10)
        



