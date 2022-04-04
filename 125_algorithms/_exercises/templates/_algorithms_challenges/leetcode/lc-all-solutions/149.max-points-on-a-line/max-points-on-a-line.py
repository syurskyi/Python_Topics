# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

c_ Solution(o..
  ___ maxPoints  points
    """
    :type points: List[Point]
    :rtype: int
    """

    ___ gcd(a, b
      w.... b:
        a, b = b, a % b
      r.. a

    ans = 1
    d    # dict
    points.s..(key=l.... p: (p.x, p.y
    ___ i __ r..(0, l..(points:
      __ i > 0 a.. (points[i].x, points[i].y) __ (points[i - 1].x, points[i - 1].y
        _____
      overlap = 1
      ___ j __ r..(i + 1, l..(points:
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
          ans = m..(ans, overlap)
        ans = m..(ans, d.get((ku, kd, x1, y1), 0) + overlap)
    r.. m..(ans, l..(points
