____ fibonacci _______ fib
_______ pytest


___ test_fib_main(n):
    ... fib(0) __ 0
    ... fib(1) __ 1
    ... fib(10) __ 55
    ... fib(20) __ 6765


___ test_fib_negative(n):
    with pytest.raises(ValueError):
        fib(-1)


