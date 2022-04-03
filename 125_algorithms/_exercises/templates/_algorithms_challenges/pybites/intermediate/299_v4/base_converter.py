___ digit_map(num
    """maps numbers greater than a single digit to letters (UPPER)"""
    r.. chr(num + 55) __ num > 9 ____ s..(num)

___ convert(number: i.., base: i.. = 2) __ s..:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """

    __ base < 2 o. base > 36:
        r.. V...

    d..    # list
    w.... number > 0:
        d...a..(number % base)
        number //= base

    d.. = l.. m..(digit_map, d..))

    r.. ''.j..(r..(d..))
