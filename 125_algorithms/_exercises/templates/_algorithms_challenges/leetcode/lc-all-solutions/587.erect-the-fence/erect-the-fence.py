# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

c_ Solution(object):
  ___ outerTrees(self, points):
    """
    :type points: List[Point]
    :rtype: List[Point]
    """
    __ l..(points) __ 1:
      r.. points

    ___ direction(p, q, r):
      r.. ((p.x - r.x) * (q.y - r.y) - (p.y - r.y) * (q.x - r.x))

    points.s..(key=l.... x: (x.x, x.y))
    upper    # list
    lower    # list
    ___ point __ points:
      w.... l..(lower) >= 2 a.. direction(lower[-2], lower[-1], point) < 0:
        lower.pop()
      lower.a..(point)

    ___ point __ r..(points):
      w.... l..(upper) >= 2 a.. direction(upper[-2], upper[-1], point) < 0:
        upper.pop()
      upper.a..(point)

    r.. l..(set(upper[1:] + lower[1:]))
