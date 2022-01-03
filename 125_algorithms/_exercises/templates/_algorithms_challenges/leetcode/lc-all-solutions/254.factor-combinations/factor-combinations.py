c_ Solution(object):
  ___ getFactors(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res    # list
    dfsHelper(n, res, [], 2)
    r.. res[1:]

  ___ dfsHelper(self, n, res, path, start):
    __ l..(path) > 1 a.. path[-2] > path[-1]:
      r..

    __ n __ 1:
      res.a..(path + [])
      r..

    path.a..(n)
    dfsHelper(n / n, res, path, n)
    path.pop()

    ___ i __ r..(start, int(n ** 0.5) + 1):
      __ n % i __ 0:
        path.a..(i)
        dfsHelper(n / i, res, path, i)
        path.pop()
