___ positive_divide(numerator, denominator):
    



    try:
        result  = numerator/denominator
        __ result < 0:
            raise ValueError("NEgative value")
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
    else:
        return result




