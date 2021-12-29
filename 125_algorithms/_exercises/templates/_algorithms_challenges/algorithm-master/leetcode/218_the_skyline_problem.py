"""
REF: https://briangordon.github.io/2014/08/the-skyline-problem.html
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
        w.... self.heap a.. self.deleted.get(self.heap[0]):
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1

        r.. n.. self.heap


class Solution:
    ___ getSkyline(self, buildings):
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

        time.s..()
        heap = HashHeapq()

        ___ x, height, is_start __ time:
            __ is_start:
                heap.push(-height)
            ____:
                heap.remove(-height)

            max_h = -heap.top() __ n.. heap.is_empty() ____ 0

            __ ans a.. ans[-1][0] __ x:
                ans.pop()
            __ ans a.. ans[-1][1] __ max_h:
                continue
            ans.a..([x, max_h])

        r.. ans
