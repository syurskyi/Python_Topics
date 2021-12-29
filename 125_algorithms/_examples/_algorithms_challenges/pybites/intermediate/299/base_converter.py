def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    if (1 < base < 37) and (isinstance(number, int)):
        base_num = ""
        while number>0:
            dig = int(number%base)
            if dig<10:
                base_num += str(dig)
            else:
                base_num += chr(ord('A')+dig-10)  #Using uppercase letters
            number //= base

        base_num = base_num[::-1]  #To reverse the string
        return base_num
    elif not (isinstance(number, int)):
        raise TypeError
    else:
        raise ValueError

#print(convert(128, 5))