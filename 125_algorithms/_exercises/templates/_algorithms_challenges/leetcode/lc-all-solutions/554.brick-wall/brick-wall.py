class Solution(object
  ___ leastBricks(self, wall
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    ans = le.(wall)
    count = 0
    d = {}
    ___ w in wall:
      coverage = 0
      ___ brick in w[:-1]:
        coverage += brick
        d[coverage] = d.get(coverage, 0) + 1
        count = max(count, d.get(coverage, 0))
    r_ ans - count
