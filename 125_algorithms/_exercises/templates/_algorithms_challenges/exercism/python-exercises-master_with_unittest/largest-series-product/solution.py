from functools import reduce
from operator import mul


___ slices(series, length):
    numbers = [int(digit) for digit in series]
    __ not 1 <= length <= len(numbers):
        raise ValueError("Invalid slice length for this series: " +
                         str(length))
    return [numbers[i:i + length]
            for i in range(len(numbers) - length + 1)]


___ largest_product(series, length):
    __ length == 0:
        return 1
    return max(reduce(mul, slc) for slc in slices(series, length))
