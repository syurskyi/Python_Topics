c_ Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne  d..
        d...r..
        res    # list
        t (d..[0] + 1) % 10
        carry (d..[0] + 1) / 10
        res.a..(t)
        ___ d __ d..[1:]:
            t (d + carry) % 10
            carry (d + carry) / 10
            res.a..(t)
        __ carry __ 1:
            res.a..(1)
        res.r..
        r.. res
