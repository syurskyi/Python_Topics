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
    __ n.. 2 <= base <= 36:
        r.. V...("Invalid Base")
    
    values    # list
    w.... number:
        remainder = number % base
        number //= base
        __ remainder >= 10:
            remainder = chr(remainder - 10  + o..('A'))

        values.a..(s..(remainder))


    r.. ''.j..(r..(values))
            









    p..
