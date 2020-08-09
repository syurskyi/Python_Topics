"""Finds largest product of slices of digits of a give size"""

___ largest_product(digits, size
    """Finds the largest product of slices of a given size"""
    # Why does a blank set of digits have a maximum product of 1?
    slice_list = slices(digits, size)
    ___ mult_reduce(items
        total = 1
        for i in items:
            total *= i
        r_ total
    slice_list = [mult_reduce(l) for l in slice_list]
    r_ max(slice_list)

___ slices(digits, size
    """Returns list of lists of consecutive digits"""
    __ not 0 <= size <= le.(digits
        raise ValueError
    ____ digits __ '':
        r_ [[1]]

    slice_list = []

    for i in range(le.(digits) - size + 1
        slice_list.append([int(d) for d in digits[i:i+size]])
    r_ slice_list
