class Solution(object
  ___ isReflected(self, points
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    __ le.(points) < 2:
      r_ True
    twoTimesMid = min(points)[0] + ma.(points)[0]
    d = set([(i, j) ___ i, j __ points])
    ___ i, j __ points:
      __ (twoTimesMid - i, j) not __ d:
        r_ False
    r_ True
