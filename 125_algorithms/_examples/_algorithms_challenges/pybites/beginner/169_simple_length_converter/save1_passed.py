def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.casefold()
    is_float = None
    while is_float is None:
        try:
            is_float = float(value)
        except TypeError:
            print('TypeError. Please input float.')
    if fmt == 'cm':
        return round(value * 2.54, 4)
    elif fmt == 'in':
        return round(value / 2.54, 4)
    else:
        raise ValueError