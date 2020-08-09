___ saddle_points(m
    __ not m:
        r_ set()
    __ any(le.(r) != le.(m[0]) ___ r in m
        raise ValueError('irregular matrix')
    mmax = [max(r) ___ r in m]
    mmin = [min(c) ___ c in zip(*m)]
    points = [(i, j) ___ i in range(le.(m))
              ___ j in range(le.(m[0])) __ mmax[i] __ mmin[j]]

    r_ set(points)
