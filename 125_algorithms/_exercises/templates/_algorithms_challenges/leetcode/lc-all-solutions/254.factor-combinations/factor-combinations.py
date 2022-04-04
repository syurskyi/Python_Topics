c_ Solution(o..
  ___ getFactors  n
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res    # list
    dfsHelper(n, res, [], 2)
    r.. res[1:]

  ___ dfsHelper  n, res, p.., start
    __ l..(p..) > 1 a.. p..[-2] > p..[-1]:
      r..

    __ n __ 1:
      res.a..(p.. + [])
      r..

    p...a..(n)
    dfsHelper(n / n, res, p.., n)
    p...p.. )

    ___ i __ r..(start, i..(n ** 0.5) + 1
      __ n % i __ 0:
        p...a..(i)
        dfsHelper(n / i, res, p.., i)
        p...p.. )
