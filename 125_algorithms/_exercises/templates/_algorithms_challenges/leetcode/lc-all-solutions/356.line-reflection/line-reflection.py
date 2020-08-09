class Solution(object
  ___ isReflected(self, points
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    __ le.(points) < 2:
      r_ True
    twoTimesMid = min(points)[0] + max(points)[0]
    d = set([(i, j) ___ i, j in points])
    ___ i, j in points:
      __ (twoTimesMid - i, j) not in d:
        r_ False
    r_ True
