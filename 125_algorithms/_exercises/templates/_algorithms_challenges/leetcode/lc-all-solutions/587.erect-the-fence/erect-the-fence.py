# Definition for a point.
# class Point(object
#     ___ __init__(self, a=0, b=0
#         self.x = a
#         self.y = b

class Solution(object
  ___ outerTrees(self, points
    """
    :type points: List[Point]
    :rtype: List[Point]
    """
    __ le.(points) __ 1:
      r_ points

    ___ direction(p, q, r
      r_ ((p.x - r.x) * (q.y - r.y) - (p.y - r.y) * (q.x - r.x))

    points.sort(key=lambda x: (x.x, x.y))
    upper = []
    lower = []
    ___ point in points:
      w___ le.(lower) >= 2 and direction(lower[-2], lower[-1], point) < 0:
        lower.p..
      lower.append(point)

    ___ point in reversed(points
      w___ le.(upper) >= 2 and direction(upper[-2], upper[-1], point) < 0:
        upper.p..
      upper.append(point)

    r_ list(set(upper[1:] + lower[1:]))
