___ slices(series, length):
    numbers = [int(digit) ___ digit __ series]
    __ n.. 1 <= length <= l..(numbers):
        raise ValueError("Invalid slice length for this series: " + str(
            length))
    r.. [numbers[i:i + length] ___ i __ r..(l..(numbers) - length + 1)]
