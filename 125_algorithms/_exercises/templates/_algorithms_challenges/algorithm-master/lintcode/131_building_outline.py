"""
this problem familiar with `leetcode/218_the_skyline_problem.py`
with different output
"""
_______ heapq


class HashHeapq:
    ___ __init__(self):
        self.heap    # list
        self.deleted = {}

    ___ push(self, val):
        heapq.heappush(self.heap, val)

    ___ pop(self):
        __ self.is_empty():
            r.. -1

        r.. heapq.heappop(self.heap)

    ___ remove(self, val):
        __ self.is_empty():
            r..

        __ val n.. __ self.deleted:
            self.deleted[val] = 0

        self.deleted[val] += 1

    ___ top(self):
        __ self.is_empty():
            r.. -1

        r.. self.heap[0]

    ___ is_empty(self):
        while self.heap and self.deleted.get(self.heap[0]):
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1

        r.. n.. self.heap


class Solution:
    ___ buildingOutline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans    # list
        __ n.. buildings:
            r.. ans

        time    # list

        ___ x, _x, height __ buildings:
            time.a..((x, height, True))
            time.a..((_x, height, False))

        time.sort()
        heap = HashHeapq()
        tmp    # list

        ___ x, height, is_start __ time:
            __ is_start:
                heap.push(-height)
            ____:
                heap.remove(-height)

            max_h = -heap.top() __ n.. heap.is_empty() ____ 0

            __ tmp and tmp[-1][0] __ x:
                tmp.pop()
            __ tmp and tmp[-1][1] __ max_h:
                continue
            tmp.a..([x, max_h])

        _x = pre_h = 0

        ___ x, height __ tmp:
            __ pre_h > 0:
                ans.a..([_x, x, pre_h])

            _x = x
            pre_h = height

        r.. ans
