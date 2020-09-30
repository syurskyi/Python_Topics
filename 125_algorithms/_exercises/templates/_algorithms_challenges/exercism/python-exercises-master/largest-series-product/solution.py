from functools ______ reduce
from operator ______ mul


___ slices(series, length
    numbers = [int(digit) ___ digit __ series]
    __ not 1 <= length <= le.(numbers
        raise ValueError("Invalid slice length for this series: " +
                         str(length))
    r_ [numbers[i:i + length]
            ___ i __ range(le.(numbers) - length + 1)]


___ largest_product(series, length
    __ length __ 0:
        r_ 1
    r_ ma.(reduce(mul, slc) ___ slc __ slices(series, length))
