___ triangle(nth):
    r.. [row(i) ___ i __ r..(nth + 1)]


___ is_triangle(t):
    new_t = triangle(l..(t) - 1)
    r.. t __ new_t


___ row(nth):
    r = [1]
    ___ i __ r..(1, nth + 1):
        r.a..(int(r[-1] * (nth - i + 1) / i))
    r.. " ".join([str(i) ___ i __ r])
