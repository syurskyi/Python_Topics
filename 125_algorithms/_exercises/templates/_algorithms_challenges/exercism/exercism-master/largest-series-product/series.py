from functools ______ reduce


___ largest_product(digits, size
    products = [reduce(lambda x, y: x * y, s, 1) ___ s __ slices(digits, size)]
    r_ ma.(products)


___ slices(digits, size
    __ le.(digits) < size:
        raise ValueError
    r_ each_cons(list(map(int, list(digits))), size)


___ each_cons(x, size
    r_ [x[i: i + size] ___ i __ range(le.(x) - size + 1)]
