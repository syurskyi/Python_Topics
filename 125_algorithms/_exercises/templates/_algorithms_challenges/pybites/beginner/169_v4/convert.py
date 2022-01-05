___ convert(value: float, fmt: s..) __ float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ n.. isi..(value, (i.., float)):
        r.. T..()
    fn = {'in': l.... x: r..(x / 2.54, 4),
          'cm': l.... x: r..(x * 2.54, 4)}
    __ fmt.l.. __ fn:
        r.. fn[fmt.l..](value)
    r.. ValueError()
