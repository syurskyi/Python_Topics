num_hundreds = -1

___ sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    total = sum(numbers)
    hundreds_value = len(list(range(0, total, 100))) - 1
    __ (total == None) or (total < 100):
        return total
    else:
        num_hundreds = num_hundreds + hundreds_value
        return total