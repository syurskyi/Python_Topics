c_ Solution(object):
  ___ isConvex(self, points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    calcDir = l.... x, y, z: (y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0])
    pre = N..
    ___ i __ r..(0, l..(points) - 2):
      x = points[i]
      y = points[i + 1]
      z = points[i + 2]
      c = calcDir(x, y, z)
      __ c __ 0:
        _____
      __ pre __ N..
        pre = c
      __ pre * c < 0:
        r.. F..
      pre = c
    __ pre * calcDir(points[-1], points[0], points[1]) < 0:
      r.. F..
    __ pre * calcDir(points[-2], points[-1], points[0]) < 0:
      r.. F..
    r.. T..
