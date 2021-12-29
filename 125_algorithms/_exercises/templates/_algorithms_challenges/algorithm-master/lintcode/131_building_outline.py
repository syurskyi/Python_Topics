"""
this problem familiar with `leetcode/218_the_skyline_problem.py`
with different output
"""
import heapq


class HashHeapq:
    ___ __init__(self):
        self.heap = []
        self.deleted = {}

    ___ push(self, val):
        heapq.heappush(self.heap, val)

    ___ pop(self):
        __ self.is_empty():
            return -1

        return heapq.heappop(self.heap)

    ___ remove(self, val):
        __ self.is_empty():
            return

        __ val not in self.deleted:
            self.deleted[val] = 0

        self.deleted[val] += 1

    ___ top(self):
        __ self.is_empty():
            return -1

        return self.heap[0]

    ___ is_empty(self):
        while self.heap and self.deleted.get(self.heap[0]):
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1

        return not self.heap


class Solution:
    ___ buildingOutline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        __ not buildings:
            return ans

        time = []

        for x, _x, height in buildings:
            time.append((x, height, True))
            time.append((_x, height, False))

        time.sort()
        heap = HashHeapq()
        tmp = []

        for x, height, is_start in time:
            __ is_start:
                heap.push(-height)
            else:
                heap.remove(-height)

            max_h = -heap.top() __ not heap.is_empty() else 0

            __ tmp and tmp[-1][0] == x:
                tmp.pop()
            __ tmp and tmp[-1][1] == max_h:
                continue
            tmp.append([x, max_h])

        _x = pre_h = 0

        for x, height in tmp:
            __ pre_h > 0:
                ans.append([_x, x, pre_h])

            _x = x
            pre_h = height

        return ans
