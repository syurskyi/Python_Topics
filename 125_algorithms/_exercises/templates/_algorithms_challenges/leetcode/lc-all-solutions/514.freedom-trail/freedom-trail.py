______ collections


class Solution(object
  ___ findRotateSteps(self, ring, key
    """
    :type ring: str
    :type key: str
    :rtype: int
    """

    ___ dfs(ring, key, pointTo, d, length, cache
      __ (pointTo, key) in cache:
        r_ cache[pointTo, key]
      __ not key:
        r_ 0
      minDist = float("inf")
      toChar = key[0]
      ___ i in d[toChar]:
        cost = min(length - abs(pointTo - i), abs(pointTo - i)) + 1
        cost += dfs(ring, key[1:], i, d, length, cache)
        minDist = min(minDist, cost)
      cache[pointTo, key] = minDist
      r_ minDist

    cache = {}
    d = collections.defaultdict(list)
    ___ i, c in enumerate(ring
      d[c].append(i)
    length = le.(ring)
    r_ dfs(ring, key, 0, d, length, cache)
