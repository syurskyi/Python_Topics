def positive_divide(numerator, denominator):
    



    try:
        result  = numerator/denominator
        if result < 0:
            raise ValueError("NEgative value")
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
    else:
        return result




