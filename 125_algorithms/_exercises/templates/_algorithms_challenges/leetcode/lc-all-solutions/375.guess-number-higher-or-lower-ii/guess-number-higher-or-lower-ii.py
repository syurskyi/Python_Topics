class Solution(object):
  ___ getMoneyAmount(self, n):
    """
    :type n: int
    :rtype: int
    """
    cache = [[0] * (n + 1) ___ _ __ r..(n + 1)]

    ___ dc(cache, start, end):
      __ start >= end:
        r.. 0
      __ cache[start][end] != 0:
        r.. cache[start][end]
      minV = float("inf")
      ___ i __ r..(start, end + 1):
        left = dc(cache, start, i - 1)
        right = dc(cache, i + 1, end)
        minV = m..(minV, max(left, right) + i)
      __ minV != float("inf"):
        cache[start][end] = minV
      r.. cache[start][end]

    dc(cache, 1, n)
    r.. cache[1][n]
