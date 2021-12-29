# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:
    ___ maxPoints(self, P):
        """
        :type P: List[Point]
        :rtype: int
        """
        ans = 0
        __ not P:
            return ans

        n = len(P)
        __ n <= 2:
            return n

        for i in range(n):
            S = {}
            points = dups = 0
            for j in range(i + 1, n):
                dx = P[i].x - P[j].x
                dy = P[i].y - P[j].y
                __ dx == 0 and dy == 0:
                    dups += 1
                    continue

                gcd = self.get_gcd(dx, dy)
                __ gcd:
                    dx //= gcd
                    dy //= gcd

                key = (dx, dy)
                S[key] = S.get(key, 0) + 1

                __ S[key] > points:
                    points = S[key]

            __ points + dups + 1 > ans:
                ans = points + dups + 1

        return ans

    ___ get_gcd(self, a, b):
        __ b == 0:
            return a
        return self.get_gcd(b, a % b)
