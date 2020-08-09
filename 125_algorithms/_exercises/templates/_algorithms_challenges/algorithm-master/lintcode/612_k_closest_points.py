"""
Definition for a point.
class Point:
    ___ __init__(self, a=0, b=0
        self.x = a
        self.y = b
"""
______ heapq


class Solution:
    """
    max heap
    """
    ___ kClosest(self, points, origin, k
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans = []

        __ not points or not origin or not k:
            r_ ans

        for i in range(le.(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(ans, (-distance, i))

            __ le.(ans) > k:
                heapq.heappop(ans)

        ans.sort(key=lambda a: (-a[0], points[a[1]].x, points[a[1]].y))

        r_ [points[i] for _, i in ans]

    ___ get_distance(self, p, q
        dx = p.x - q.x
        dy = p.y - q.y
        r_ dx * dx + dy * dy


______ heapq


class Solution:
    """
    min heap
    """
    ___ kClosest(self, points, origin, k
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans = []

        __ not points or not origin or not k:
            r_ ans

        heap = []

        for i in range(le.(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(heap, (distance, i))

        for _ in range(k
            distance, i = heapq.heappop(heap)
            ans.append((distance, points[i]))

        ans.sort(key=lambda a: (a[0], a[1].x, a[1].y))

        r_ [p for _, p in ans]

    ___ get_distance(self, p, q
        dx = p.x - q.x
        dy = p.y - q.y
        r_ dx * dx + dy * dy
