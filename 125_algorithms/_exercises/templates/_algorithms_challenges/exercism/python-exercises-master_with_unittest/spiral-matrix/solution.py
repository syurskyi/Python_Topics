___ spiral(size):
    sm = [[0]*size ___ k __ r..(size)]
    i, j, el = 0, -1, 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    ___ x __ r..(2*size - 1):
        ___ y __ r..((2*size - x) // 2):
            i += di[x % 4]
            j += dj[x % 4]
            sm[i][j] = el
            el += 1
    r.. sm
