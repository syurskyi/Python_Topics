c_ Solution(o..
  ___ getMoneyAmount  n
    """
    :type n: int
    :rtype: int
    """
    cache [[0] * (n + 1) ___ _ __ r..(n + 1)]

    ___ dc(cache, start, end
      __ start >_ end:
        r.. 0
      __ cache[start][end] !_ 0:
        r.. cache[start][end]
      minV f__("inf")
      ___ i __ r..(start, end + 1
        left dc(cache, start, i - 1)
        right dc(cache, i + 1, end)
        minV m..(minV, m..(left, right) + i)
      __ minV !_ f__("inf"
        cache[start][end] minV
      r.. cache[start][end]

    dc(cache, 1, n)
    r.. cache[1][n]
