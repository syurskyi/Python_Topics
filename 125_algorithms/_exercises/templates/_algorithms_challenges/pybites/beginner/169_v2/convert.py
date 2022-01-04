___ convert(value: float, fmt: s..) __ float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """


    __ t..(value) n.. __ (i..,float):
        raise TypeError("Value must be numeric")

    fmt = fmt.s...l..
    __ fmt n.. __ ('cm','in'):
        raise ValueError("Can only convert from cm to in or vice versa")


    __ fmt __ 'in':
        value /= 2.54
    ____:
        value  *= 2.54


    r.. round(value,4)

















