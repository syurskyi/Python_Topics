def positive_divide(numerator, denominator):
    try:
        output = numerator / denominator        
        if output < 0:
            raise ValueError
        if not isinstance(output, (int, float)):
            print('Values must be numbers.')
        else:
            return output
    except ZeroDivisionError:
        return 0
