_______ pytest
____ fibonacci _______ fib


# write one or more pytest functions below, they need to start with test_
___ test_fib_zero
    ... fib(0) __ 0


___ test_fib_neg
    with pytest.raises(ValueError):
        fib(-1)


___ test_fib_pos
    ... fib(1) __ 1
    ... fib(10) __ 55
