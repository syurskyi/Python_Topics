def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """


    if type(value) not in (int,float):
        raise TypeError("Value must be numeric")

    fmt = fmt.strip().lower() 
    if fmt not in ('cm','in'):
        raise ValueError("Can only convert from cm to in or vice versa")


    if fmt == 'in':
        value /= 2.54
    else:
        value  *= 2.54


    return round(value,4)

















