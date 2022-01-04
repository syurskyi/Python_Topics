_______ pytest
____ fibonacci _______ fib

# write one or more pytest functions below, they need to start with test_

___ test_ValueError
    with pytest.raises(ValueError):
        fib(-1)

___ test_simple
    ... fib(4) __ 3
    ... fib(5) __ 5
    ... fib(6) __ 8
    ... fib(10) __ 55