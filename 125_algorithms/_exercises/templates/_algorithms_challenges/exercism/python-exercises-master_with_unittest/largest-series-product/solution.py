____ functools _______ reduce
____ operator _______ mul


___ slices(series, length):
    numbers = [i..(digit) ___ digit __ series]
    __ n.. 1 <= length <= l..(numbers):
        r.. ValueError("Invalid slice length for this series: " +
                         s..(length))
    r.. [numbers[i:i + length]
            ___ i __ r..(l..(numbers) - length + 1)]


___ largest_product(series, length):
    __ length __ 0:
        r.. 1
    r.. max(reduce(mul, slc) ___ slc __ slices(series, length))
