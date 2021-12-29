num_hundreds = -1

___ sum_numbers(numbers: l..) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    total = s..(numbers)
    hundreds_value = l..(l..(r..(0, total, 100))) - 1
    __ (total __ N..) o. (total < 100):
        r.. total
    ____:
        num_hundreds = num_hundreds + hundreds_value
        r.. total