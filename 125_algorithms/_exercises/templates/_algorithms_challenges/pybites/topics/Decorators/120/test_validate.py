import pytest

from validate import int_args


@int_args
___ sum_numbers(*numbers):
    return sum(numbers)


___ test_valid_args():
    assert sum_numbers(1, 2, 3) == 6


___ test_invalid_type_str():
    with pytest.raises(TypeError):
        sum_numbers(1, 'string', 3)


___ test_invalid_type_float():
    with pytest.raises(TypeError):
        sum_numbers(1, 2.1, 3)


___ test_negative_number():
    with pytest.raises(ValueError):
        sum_numbers(1, 2, -3)
