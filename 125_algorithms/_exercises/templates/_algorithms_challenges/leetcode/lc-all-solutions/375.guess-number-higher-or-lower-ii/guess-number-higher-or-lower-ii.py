class Solution(object):
  ___ getMoneyAmount(self, n):
    """
    :type n: int
    :rtype: int
    """
    cache = [[0] * (n + 1) for _ in range(n + 1)]

    ___ dc(cache, start, end):
      __ start >= end:
        return 0
      __ cache[start][end] != 0:
        return cache[start][end]
      minV = float("inf")
      for i in range(start, end + 1):
        left = dc(cache, start, i - 1)
        right = dc(cache, i + 1, end)
        minV = min(minV, max(left, right) + i)
      __ minV != float("inf"):
        cache[start][end] = minV
      return cache[start][end]

    dc(cache, 1, n)
    return cache[1][n]
