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
    __ not 2 <= base <= 36:
        raise ValueError("Invalid Base")
    
    values = []
    while number:
        remainder = number % base
        number //= base
        __ remainder >= 10:
            remainder = chr(remainder - 10  + ord('A'))

        values.append(str(remainder))


    return ''.join(reversed(values))
            









    pass
