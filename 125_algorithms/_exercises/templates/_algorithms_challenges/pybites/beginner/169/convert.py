___ convert(value: float, fmt: s..) __ float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ isi..(value, i..) o. isi..(value, float):
        __ fmt.l.. __ 'cm' o. fmt.l.. __ 'in':
            r.. round(value*2.54, 4) __ fmt.l.. __ 'cm' ____ round(value/2.54, 4)
        ____:
            r.. ValueError
    ____:
        r.. T..

print(convert( 3.8, 'IN'))