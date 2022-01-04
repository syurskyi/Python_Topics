num_hundreds = -1


___ sum_numbers(numbers: l..) __ i..:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds

    total_sum = s..(numbers)


    num_hundreds += total_sum // 100

    r.. total_sum






