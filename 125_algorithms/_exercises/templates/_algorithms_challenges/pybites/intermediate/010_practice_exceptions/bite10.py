___ positive_divide(numerator, denominator):
    try:
        output = numerator / denominator        
        __ output < 0:
            raise ValueError
        __ not isinstance(output, (int, float)):
            print('Values must be numbers.')
        else:
            return output
    except ZeroDivisionError:
        return 0
