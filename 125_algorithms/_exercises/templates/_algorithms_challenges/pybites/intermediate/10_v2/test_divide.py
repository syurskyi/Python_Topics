_______ p__

____ divide _______ positive_divide


___ test_positive_divide_good_values
    ... positive_divide(1, 2) __ 0.5
    ... positive_divide(1, 0) __ 0
    ... positive_divide(-1, -2) __ 0.5
    ... positive_divide(1.5, 2) __ 0.75


___ test_positive_divide_exceptions
    ___
        positive_divide(2, 0)
    ______ ZeroDivisionError:
        p__.fail("Unexpected ZeroDivisionError!")
    w__ p__.r.. T..
        positive_divide(1, 's')
        positive_divide([], 2)
    w__ p__.r..(ValueError
        positive_divide(1, -2)
        positive_divide(-1, 2)
