___ convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.casefold()
    is_float = N..
    while is_float __ N..
        try:
            is_float = float(value)
        except TypeError:
            print('TypeError. Please input float.')
    __ fmt __ 'cm':
        r.. round(value * 2.54, 4)
    ____ fmt __ 'in':
        r.. round(value / 2.54, 4)
    ____:
        raise ValueError