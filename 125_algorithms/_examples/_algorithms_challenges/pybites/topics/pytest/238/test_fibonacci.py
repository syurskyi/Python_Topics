import pytest
from fibonacci import fib

# write one or more pytest functions below, they need to start with test_

def test_ValueError():
    with pytest.raises(ValueError):
        fib(-1)

def test_simple():
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(10) == 55