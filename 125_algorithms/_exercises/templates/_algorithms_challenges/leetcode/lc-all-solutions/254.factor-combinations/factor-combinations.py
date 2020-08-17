class Solution(object
  ___ getFactors(self, n
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    self.dfsHelper(n, res, [], 2)
    r_ res[1:]

  ___ dfsHelper(self, n, res, path, start
    __ le.(path) > 1 and path[-2] > path[-1]:
      r_

    __ n __ 1:
      res.append(path + [])
      r_

    path.append(n)
    self.dfsHelper(n / n, res, path, n)
    path.p..

    ___ i in range(start, int(n ** 0.5) + 1
      __ n % i __ 0:
        path.append(i)
        self.dfsHelper(n / i, res, path, i)
        path.p..
