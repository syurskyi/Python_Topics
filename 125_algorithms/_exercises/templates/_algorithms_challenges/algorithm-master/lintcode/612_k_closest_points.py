"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
_______ heapq


class Solution:
    """
    max heap
    """
    ___ kClosest(self, points, origin, k):
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans    # list

        __ n.. points o. n.. origin o. n.. k:
            r.. ans

        ___ i __ r..(l..(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(ans, (-distance, i))

            __ l..(ans) > k:
                heapq.heappop(ans)

        ans.s..(key=l.... a: (-a[0], points[a[1]].x, points[a[1]].y))

        r.. [points[i] ___ _, i __ ans]

    ___ get_distance(self, p, q):
        dx = p.x - q.x
        dy = p.y - q.y
        r.. dx * dx + dy * dy


_______ heapq


class Solution:
    """
    min heap
    """
    ___ kClosest(self, points, origin, k):
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans    # list

        __ n.. points o. n.. origin o. n.. k:
            r.. ans

        heap    # list

        ___ i __ r..(l..(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(heap, (distance, i))

        ___ _ __ r..(k):
            distance, i = heapq.heappop(heap)
            ans.a..((distance, points[i]))

        ans.s..(key=l.... a: (a[0], a[1].x, a[1].y))

        r.. [p ___ _, p __ ans]

    ___ get_distance(self, p, q):
        dx = p.x - q.x
        dy = p.y - q.y
        r.. dx * dx + dy * dy
