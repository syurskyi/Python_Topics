___ convert(number: i.., base: i.. 2) __ s..:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    __ (1 < base < 37) a.. (isi..(number, i..:
        base_num ""
        w.... number>0:
            dig i..(number%base)
            __ dig<10:
                base_num += s..(dig)
            ____
                base_num += chr(o..('A')+dig-10)  #Using uppercase letters
            number //= base

        base_num base_num[::-1]  #To reverse the string
        r.. base_num
    ____ n.. (isi..(number, i..:
        r.. T..
    ____
        r.. V...

#print(convert(128, 5))