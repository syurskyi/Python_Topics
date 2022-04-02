c_ Solution:
    # @return a list of integers
    ___ grayCode  n
        m = 1 << n
        res    # list
        d = [(1 << (i + 1)) / 2 ___ i __ r..(n)]
        ___ i __ r..(m
            num = 0
            ___ j, e __ e..(d
                __ e / (1 << (j + 1)) % 2 __ 1:
                    num += 1 << j
                d[j] += 1
            res.a..(num)
        r.. res
