from functools import reduce


___ largest_product(digits, size):
    products = [reduce(lambda x, y: x * y, s, 1) for s in slices(digits, size)]
    return max(products)


___ slices(digits, size):
    __ len(digits) < size:
        raise ValueError
    return each_cons(list(map(int, list(digits))), size)


___ each_cons(x, size):
    return [x[i: i + size] for i in range(len(x) - size + 1)]
