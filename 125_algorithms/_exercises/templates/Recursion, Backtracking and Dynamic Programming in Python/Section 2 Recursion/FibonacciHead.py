
___ fibonacci_head(n

    __ n __ 0:
        r_ 0
    __ n __ 1:
        r_ 1

    # we make the recursive function call(s)
    # we are going to do 2 recursion - we keep calculating the fibonacci numbers
    # some values are calculate twice - there are multiple stack frames with the same value
    fib1 = fibonacci_head(n-1)
    fib2 = fibonacci_head(n-2)

    # make some operations
    result = fib1 + fib2

    r_ result


print(fibonacci_head(20))
