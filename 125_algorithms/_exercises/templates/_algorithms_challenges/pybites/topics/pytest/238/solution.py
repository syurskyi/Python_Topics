import pytest

from fibonacci import fib


___ test_base_case():
    assert fib(0) == 0
    assert fib(1) == 1


___ test_higher_number():
    assert fib(10) == 55


___ test_negative_number():
    with pytest.raises(ValueError):
        fib(-1)