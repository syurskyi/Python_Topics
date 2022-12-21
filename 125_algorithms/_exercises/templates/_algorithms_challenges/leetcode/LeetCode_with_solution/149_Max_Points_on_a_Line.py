# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

c_ Solution o..
    ___ maxPoints  points
        """
        :type points: List[Point]
        :rtype: int
        """
        # map all possible angle
        __ points is N.. or l.. points) __ 0:
            r_ 0
        ls = l.. points)
        res = 0
        ___ i __ r.. ls
            line_map  # dict
            overlap = max_point = 0
            ___ j __ r.. i + 1, ls
                x, y = points[j].x - points[i].x, points[j].y - points[i].y
                __ x __ 0 and y __ 0:
                    overlap += 1
                    c_
                gcd = generateGCD(x, y)
                __ gcd != 0:
                    x /= gcd
                    y /= gcd
                __ x __ line_map:
                    __ y __ line_map[x]:
                        line_map[x][y] += 1
                    ____
                        line_map[x][y] = 1
                ____
                    line_map[x]  # dict
                    line_map[x][y] = 1
                max_point = m..(max_point, line_map[x][y])
            res = m..(res, max_point + overlap + 1)
        r_ res

    ___ generateGCD  x, y
        __ y __ 0:
            r_ x
        ____
            r_ generateGCD(y, x % y)

