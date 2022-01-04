_______ pytest

____ fibonacci _______ fib


___ test_base_case
    ... fib(0) __ 0
    ... fib(1) __ 1


___ test_higher_number
    ... fib(10) __ 55


___ test_negative_number
    with pytest.raises(ValueError):
        fib(-1)