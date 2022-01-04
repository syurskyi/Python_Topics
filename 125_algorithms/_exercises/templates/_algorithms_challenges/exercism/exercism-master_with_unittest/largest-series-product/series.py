____ functools _______ reduce


___ largest_product(d.., size):
    products = [reduce(l.... x, y: x * y, s, 1) ___ s __ slices(d.., size)]
    r.. max(products)


___ slices(d.., size):
    __ l..(d..) < size:
        raise ValueError
    r.. each_cons(l..(map(int, l..(d..))), size)


___ each_cons(x, size):
    r.. [x[i: i + size] ___ i __ r..(l..(x) - size + 1)]
