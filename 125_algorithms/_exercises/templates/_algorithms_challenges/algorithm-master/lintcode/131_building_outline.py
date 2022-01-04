"""
this problem familiar with `leetcode/218_the_skyline_problem.py`
with different output
"""
_______ heapq


c_ HashHeapq:
    ___ - ):
        heap    # list
        deleted    # dict

    ___ push(self, val):
        heapq.heappush(heap, val)

    ___ pop
        __ is_empty
            r.. -1

        r.. heapq.heappop(heap)

    ___ remove(self, val):
        __ is_empty
            r..

        __ val n.. __ deleted:
            deleted[val] = 0

        deleted[val] += 1

    ___ top
        __ is_empty
            r.. -1

        r.. heap[0]

    ___ is_empty
        w.... heap a.. deleted.get(heap[0]):
            val = heapq.heappop(heap)
            deleted[val] -= 1

        r.. n.. heap


c_ Solution:
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
            time.a..((x, height, T..))
            time.a..((_x, height, F..))

        time.s..()
        heap = HashHeapq()
        tmp    # list

        ___ x, height, is_start __ time:
            __ is_start:
                heap.push(-height)
            ____:
                heap.remove(-height)

            max_h = -heap.top() __ n.. heap.is_empty() ____ 0

            __ tmp a.. tmp[-1][0] __ x:
                tmp.pop()
            __ tmp a.. tmp[-1][1] __ max_h:
                continue
            tmp.a..([x, max_h])

        _x = pre_h = 0

        ___ x, height __ tmp:
            __ pre_h > 0:
                ans.a..([_x, x, pre_h])

            _x = x
            pre_h = height

        r.. ans
