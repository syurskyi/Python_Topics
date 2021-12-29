import pytest

from fibonacci import fib


def test_base_case():
    assert fib(0) == 0
    assert fib(1) == 1


def test_higher_number():
    assert fib(10) == 55


def test_negative_number():
    with pytest.raises(ValueError):
        fib(-1)