from fibonacci import fib
import pytest


___ test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8


___ test_fib_negative():
    with pytest.raises(ValueError):
        fib(-10)
        



