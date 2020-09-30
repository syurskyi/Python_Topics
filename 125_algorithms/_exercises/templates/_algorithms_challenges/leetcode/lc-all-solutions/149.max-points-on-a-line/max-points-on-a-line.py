# Definition for a point.
# class Point(object
#     ___ __init__(self, a=0, b=0
#         self.x = a
#         self.y = b

class Solution(object
  ___ maxPoints(self, points
    """
    :type points: List[Point]
    :rtype: int
    """

    ___ gcd(a, b
      w___ b:
        a, b = b, a % b
      r_ a

    ans = 1
    d = {}
    points.sort(key=lambda p: (p.x, p.y))
    ___ i __ range(0, le.(points)):
      __ i > 0 and (points[i].x, points[i].y) __ (points[i - 1].x, points[i - 1].y
        continue
      overlap = 1
      ___ j __ range(i + 1, le.(points)):
        x1, y1 = points[i].x, points[i].y
        x2, y2 = points[j].x, points[j].y
        ku, kd = y2 - y1, x2 - x1
        __ (x1, y1) != (x2, y2
          kg = gcd(ku, kd)
          ku /= kg
          kd /= kg
          d[(ku, kd, x1, y1)] = d.get((ku, kd, x1, y1), 0) + 1
        ____
          overlap += 1
          ans = ma.(ans, overlap)
        ans = ma.(ans, d.get((ku, kd, x1, y1), 0) + overlap)
    r_ min(ans, le.(points))
