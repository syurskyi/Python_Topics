c_ Solution:
    """
    @param: k: An integer
    @param: n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    ___ digitCounts  k, n
        ans 0
        ___ i __ r..(n + 1
            ans += c.. k, i)
        r.. ans

    ___ c..  - k, a
        __ k __ a __ 0:
            r.. 1

        cnt 0
        w.... a:
            __ a % 10 __ k:
                cnt += 1
            a //= 10
        r.. cnt
