____ functools _______ reduce


___ largest_product(digits, size):
    products = [reduce(l.... x, y: x * y, s, 1) ___ s __ slices(digits, size)]
    r.. max(products)


___ slices(digits, size):
    __ l..(digits) < size:
        raise ValueError
    r.. each_cons(l..(map(int, l..(digits))), size)


___ each_cons(x, size):
    r.. [x[i: i + size] ___ i __ r..(l..(x) - size + 1)]
