class Solution(object):
  ___ isReflected(self, points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    __ len(points) < 2:
      return True
    twoTimesMid = min(points)[0] + max(points)[0]
    d = set([(i, j) for i, j in points])
    for i, j in points:
      __ (twoTimesMid - i, j) not in d:
        return False
    return True
