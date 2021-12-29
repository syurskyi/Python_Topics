___ convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    __ isi..(value, int) o. isi..(value, float):
        __ fmt.lower() __ 'cm' o. fmt.lower() __ 'in':
            r.. round(value*2.54, 4) __ fmt.lower() __ 'cm' ____ round(value/2.54, 4)
        ____:
            raise ValueError
    ____:
        raise TypeError

print(convert( 3.8, 'IN'))