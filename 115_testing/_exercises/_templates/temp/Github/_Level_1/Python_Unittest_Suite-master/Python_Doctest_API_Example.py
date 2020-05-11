# Python Doctest API
# The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work
# exactly as shown.
#
#  There are several common ways to use doctest:
# > To check that a module�s docstrings are up-to-date by verifying that all interactive examples still work as documented.
# > To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
# > To write tutorial documentation for a package, liberally illustrated with input-output examples.
#   Depending on whether the examples or the expository text are emphasized, this has the flavor of �literate testing� or �executable documentation�.
#
 
#
# Here�s a complete but small example module:
# 

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

___ factorial(n
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
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
    265252859812191058636308480000000

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
