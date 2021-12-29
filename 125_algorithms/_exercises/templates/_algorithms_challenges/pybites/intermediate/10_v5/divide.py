___ positive_divide(numerator, denominator):
    __ denominator == 0:
        return 0
    try:
        result = numerator / denominator
        __ result < 0:
            raise ValueError()
    except TypeError as e:
        raise e
    return result
