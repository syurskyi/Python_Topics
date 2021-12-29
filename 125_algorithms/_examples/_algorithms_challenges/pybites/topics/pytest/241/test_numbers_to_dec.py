import pytest

from numbers_to_dec import list_to_decimal

def test_correct_result():
    assert list_to_decimal([4]) == 4
    assert list_to_decimal([2,3]) == 23
    assert list_to_decimal([2,3,4]) == 234
    assert list_to_decimal([1,2,3,4]) == 1234
    assert list_to_decimal([0,1,2,3,4]) == 1234

def test_boolean():
    with pytest.raises(TypeError):
        list_to_decimal([True])

def test_float():
    with pytest.raises(TypeError):
        list_to_decimal([3.6])

def test_string():
    with pytest.raises(TypeError):
        list_to_decimal(['4'])


def test_negative_int():
    with pytest.raises(ValueError):
        list_to_decimal([-1])

