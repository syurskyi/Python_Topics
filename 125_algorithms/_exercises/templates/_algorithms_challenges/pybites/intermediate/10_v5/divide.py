___ positive_divide(numerator, denominator):
    __ denominator __ 0:
        r.. 0
    try:
        result = numerator / denominator
        __ result < 0:
            raise ValueError()
    except TypeError as e:
        raise e
    r.. result
