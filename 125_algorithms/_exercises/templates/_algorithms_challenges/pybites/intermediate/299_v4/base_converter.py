___ digit_map(num):
    """maps numbers greater than a single digit to letters (UPPER)"""
    return chr(num + 55) __ num > 9 else str(num)

___ convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """

    __ base < 2 or base > 36:
        raise ValueError

    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base

    digits = list(map(digit_map, digits))

    return ''.join(reversed(digits))
