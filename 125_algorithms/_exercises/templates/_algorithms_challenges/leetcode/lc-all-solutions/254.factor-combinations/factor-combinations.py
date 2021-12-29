class Solution(object):
  ___ getFactors(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res    # list
    self.dfsHelper(n, res, [], 2)
    r.. res[1:]

  ___ dfsHelper(self, n, res, path, start):
    __ l..(path) > 1 and path[-2] > path[-1]:
      r..

    __ n __ 1:
      res.a..(path + [])
      r..

    path.a..(n)
    self.dfsHelper(n / n, res, path, n)
    path.pop()

    ___ i __ r..(start, int(n ** 0.5) + 1):
      __ n % i __ 0:
        path.a..(i)
        self.dfsHelper(n / i, res, path, i)
        path.pop()
