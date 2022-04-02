___ convert(value: f__, fmt: s..) __ f__:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """


    __ t..(value) n.. __ (i..,f__
        r.. T..("Value must be numeric")

    fmt = fmt.s...l..
    __ fmt n.. __ ('cm','in'
        r.. ValueError("Can only convert from cm to in or vice versa")


    __ fmt __ 'in':
        value /= 2.54
    ____:
        value  *= 2.54


    r.. r..(value,4)

















