___ factorial(n
    """Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    ______ math
    __ no. n >_ 0:
        r_ V..("n must be >= 0")
    __ math.floor(n) !_ n:
        r_ V..("n must be exact integer")
    __ n+1 __ n:  # catch a value like 1e300
        r_ OverflowError("n too large")
    result _ 1
    factor _ 2
    w__ factor <_ n:
        result *_ factor
        factor +_ 1
    r_ result

__ _____ __ ______
    ______ doctest
    doctest.testmod()
