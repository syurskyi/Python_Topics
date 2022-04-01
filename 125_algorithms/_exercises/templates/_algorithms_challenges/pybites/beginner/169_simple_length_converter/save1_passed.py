___ convert(value: f__, fmt: s..) __ f__:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.casefold()
    is_float = N..
    w.... is_float __ N..
        ___
            is_float = f__(value)
        ______ T..:
            print('TypeError. Please input float.')
    __ fmt __ 'cm':
        r.. r..(value * 2.54, 4)
    ____ fmt __ 'in':
        r.. r..(value / 2.54, 4)
    ____:
        r.. ValueError