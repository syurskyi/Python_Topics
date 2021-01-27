
___ factorial_head(n

    # this is the base case - 0!=1
    __ n __ 0:
        r_ 1

    # use recursion
    result1 = factorial_head(n-1)

    # we do some operations
    result2 = n * result1
    r_ result2


___ factorial_tail(n, accumulator=1

    __ n __ 1:
        r_ accumulator

    r_ factorial_tail(n-1, n * accumulator)


print(factorial_tail(4))
