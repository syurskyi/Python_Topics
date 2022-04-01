___ saddle_points(m):
    __ n.. m:
        r.. s..()
    __ any(l..(r) != l..(m[0]) ___ r __ m):
        r.. ValueError('irregular matrix')
    mmax = [m..(r) ___ r __ m]
    mmin = [m..(c) ___ c __ z..(*m)]
    points = [(i, j) ___ i __ r..(l..(m))
              ___ j __ r..(l..(m[0])) __ mmax[i] __ mmin[j]]

    r.. s..(points)
