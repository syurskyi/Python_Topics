_______ pytest

____ divide _______ positive_divide


___ test_positive_divide_good_values():
    ... positive_divide(1, 2) __ 0.5
    ... positive_divide(1, 0) __ 0
    ... positive_divide(-1, -2) __ 0.5
    ... positive_divide(1.5, 2) __ 0.75


___ test_positive_divide_exceptions():
    try:
        positive_divide(2, 0)
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError!")
    with pytest.raises(TypeError):
        positive_divide(1, 's')
        positive_divide([], 2)
    with pytest.raises(ValueError):
        positive_divide(1, -2)
        positive_divide(-1, 2)
