_______ c..


c_ Solution(object):
  ___ findRotateSteps  ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """

    ___ dfs(ring, key, pointTo, d, length, cache):
      __ (pointTo, key) __ cache:
        r.. cache[pointTo, key]
      __ n.. key:
        r.. 0
      minDist = float("inf")
      toChar = key[0]
      ___ i __ d[toChar]:
        cost = m..(length - abs(pointTo - i), abs(pointTo - i)) + 1
        cost += dfs(ring, key[1:], i, d, length, cache)
        minDist = m..(minDist, cost)
      cache[pointTo, key] = minDist
      r.. minDist

    cache    # dict
    d = c...defaultdict(l..)
    ___ i, c __ e..(ring):
      d[c].a..(i)
    length = l..(ring)
    r.. dfs(ring, key, 0, d, length, cache)
