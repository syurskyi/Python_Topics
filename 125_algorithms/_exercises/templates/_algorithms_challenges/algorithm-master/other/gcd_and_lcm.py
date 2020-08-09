___ get_gcd(a, b
    """
    :type a: int
    :type b: int
    :rtype: int

    >>> get_gcd(10, 2)
    2
    >>> get_gcd(500, 375)
    125
    """
    w___ b:
        a, b = b, a % b
    r_ a


___ get_lcm(a, b
    """
    :type a: int
    :type b: int
    :rtype: int

    >>> get_lcm(10, 2)
    10
    >>> get_lcm(500, 375)
    1500
    """
    r_ (a * b) // get_gcd(a, b)
