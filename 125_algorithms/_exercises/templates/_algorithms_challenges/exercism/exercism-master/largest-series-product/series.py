from functools ______ reduce


___ largest_product(digits, size
    products = [reduce(lambda x, y: x * y, s, 1) ___ s in slices(digits, size)]
    r_ max(products)


___ slices(digits, size
    __ le.(digits) < size:
        raise ValueError
    r_ each_cons(list(map(int, list(digits))), size)


___ each_cons(x, size
    r_ [x[i: i + size] ___ i in range(le.(x) - size + 1)]
