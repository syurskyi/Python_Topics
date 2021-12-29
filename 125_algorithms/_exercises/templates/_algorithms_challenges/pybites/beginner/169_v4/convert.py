___ convert(value: float, fmt: s..) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ n.. isi..(value, (int, float)):
        raise TypeError()
    fn = {'in': l.... x: round(x / 2.54, 4),
          'cm': l.... x: round(x * 2.54, 4)}
    __ fmt.lower() __ fn:
        r.. fn[fmt.lower()](value)
    raise ValueError()
