def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if isinstance(value, int) or isinstance(value, float):
        if fmt.lower() == 'cm' or fmt.lower() == 'in':
            return round(value*2.54, 4) if fmt.lower() == 'cm' else round(value/2.54, 4)
        else:
            raise ValueError
    else:
        raise TypeError

print(convert( 3.8, 'IN'))