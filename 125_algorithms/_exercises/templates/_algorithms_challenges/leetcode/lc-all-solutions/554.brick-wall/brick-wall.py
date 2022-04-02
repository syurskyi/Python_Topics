c_ Solution(o..
  ___ leastBricks  wall
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    ans = l..(wall)
    count = 0
    d    # dict
    ___ w __ wall:
      coverage = 0
      ___ brick __ w[:-1]:
        coverage += brick
        d[coverage] = d.get(coverage, 0) + 1
        count = m..(count, d.get(coverage, 0))
    r.. ans - count
