___ triangle(nth
    r_ [row(i) for i in range(nth + 1)]


___ is_triangle(t
    new_t = triangle(le.(t) - 1)
    r_ t __ new_t


___ row(nth
    r = [1]
    for i in range(1, nth + 1
        r.append(int(r[-1] * (nth - i + 1) / i))
    r_ " ".join([str(i) for i in r])
