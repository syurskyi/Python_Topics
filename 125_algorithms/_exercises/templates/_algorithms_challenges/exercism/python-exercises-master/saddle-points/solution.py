___ saddle_points(m
    __ not m:
        r_ set()
    __ any(le.(r) != le.(m[0]) for r in m
        raise ValueError('irregular matrix')
    mmax = [max(r) for r in m]
    mmin = [min(c) for c in zip(*m)]
    points = [(i, j) for i in range(le.(m))
              for j in range(le.(m[0])) __ mmax[i] __ mmin[j]]

    r_ set(points)
