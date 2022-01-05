# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


c_ Solution:
    ___ maxPoints  P):
        """
        :type P: List[Point]
        :rtype: int
        """
        ans = 0
        __ n.. P:
            r.. ans

        n = l..(P)
        __ n <= 2:
            r.. n

        ___ i __ r..(n):
            S    # dict
            points = dups = 0
            ___ j __ r..(i + 1, n):
                dx = P[i].x - P[j].x
                dy = P[i].y - P[j].y
                __ dx __ 0 a.. dy __ 0:
                    dups += 1
                    _____

                gcd = get_gcd(dx, dy)
                __ gcd:
                    dx //= gcd
                    dy //= gcd

                key = (dx, dy)
                S[key] = S.get(key, 0) + 1

                __ S[key] > points:
                    points = S[key]

            __ points + dups + 1 > ans:
                ans = points + dups + 1

        r.. ans

    ___ get_gcd  a, b):
        __ b __ 0:
            r.. a
        r.. get_gcd(b, a % b)
