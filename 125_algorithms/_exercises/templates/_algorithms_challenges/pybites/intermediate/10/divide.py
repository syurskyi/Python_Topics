___ positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise

    __ result < 0:
        raise ValueError
    else:
        return result    