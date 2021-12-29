___ convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ isinstance(value, int) or isinstance(value, float):
        __ fmt.lower() == 'cm' or fmt.lower() == 'in':
            return round(value*2.54, 4) __ fmt.lower() == 'cm' else round(value/2.54, 4)
        else:
            raise ValueError
    else:
        raise TypeError

print(convert( 3.8, 'IN'))