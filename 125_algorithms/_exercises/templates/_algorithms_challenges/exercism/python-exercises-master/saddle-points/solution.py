___ saddle_points(m
    __ not m:
        r_ set()
    __ any(le.(r) != le.(m[0]) ___ r __ m
        raise ValueError('irregular matrix')
    mmax = [ma.(r) ___ r __ m]
    mmin = [min(c) ___ c __ zip(*m)]
    points = [(i, j) ___ i __ range(le.(m))
              ___ j __ range(le.(m[0])) __ mmax[i] __ mmin[j]]

    r_ set(points)
