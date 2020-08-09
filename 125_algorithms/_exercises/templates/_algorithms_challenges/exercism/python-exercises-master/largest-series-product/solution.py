from functools ______ reduce
from operator ______ mul


___ slices(series, length
    numbers = [int(digit) for digit in series]
    __ not 1 <= length <= le.(numbers
        raise ValueError("Invalid slice length for this series: " +
                         str(length))
    r_ [numbers[i:i + length]
            for i in range(le.(numbers) - length + 1)]


___ largest_product(series, length
    __ length __ 0:
        r_ 1
    r_ max(reduce(mul, slc) for slc in slices(series, length))
