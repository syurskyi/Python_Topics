___ saddle_points(m):
    __ not m:
        return set()
    __ any(len(r) != len(m[0]) for r in m):
        raise ValueError('irregular matrix')
    mmax = [max(r) for r in m]
    mmin = [min(c) for c in zip(*m)]
    points = [(i, j) for i in range(len(m))
              for j in range(len(m[0])) __ mmax[i] == mmin[j]]

    return set(points)
