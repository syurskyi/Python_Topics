class Solution(object):
  ___ isConvex(self, points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    calcDir = lambda x, y, z: (y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0])
    pre = None
    for i in range(0, len(points) - 2):
      x = points[i]
      y = points[i + 1]
      z = points[i + 2]
      c = calcDir(x, y, z)
      __ c == 0:
        continue
      __ pre is None:
        pre = c
      __ pre * c < 0:
        return False
      pre = c
    __ pre * calcDir(points[-1], points[0], points[1]) < 0:
      return False
    __ pre * calcDir(points[-2], points[-1], points[0]) < 0:
      return False
    return True
