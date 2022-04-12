"""
this problem familiar with `leetcode/218_the_skyline_problem.py`
with different output
"""
_______ h__


c_ HashHeapq:
    ___ -
        heap    # list
        deleted    # dict

    ___ push  val
        h__.heappush(heap, val)

    ___ pop
        __ is_empty
            r.. -1

        r.. h__.heappop(heap)

    ___ remove  val
        __ is_empty
            r..

        __ val n.. __ deleted:
            deleted[val] 0

        deleted[val] += 1

    ___ top
        __ is_empty
            r.. -1

        r.. heap[0]

    ___ is_empty
        w.... heap a.. deleted.g.. heap[0]
            val h__.heappop(heap)
            deleted[val] -_ 1

        r.. n.. heap


c_ Solution:
    ___ buildingOutline  buildings
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans    # list
        __ n.. buildings:
            r.. ans

        t__    # list

        ___ x, _x, height __ buildings:
            t__.a..((x, height, T..
            t__.a..((_x, height, F..

        t__.s..()
        heap HashHeapq()
        tmp    # list

        ___ x, height, is_start __ t__:
            __ is_start:
                heap.push(-height)
            ____
                heap.remove(-height)

            max_h -heap.top() __ n.. heap.is_empty() ____ 0

            __ tmp a.. tmp[-1][0] __ x:
                tmp.p.. )
            __ tmp a.. tmp[-1][1] __ max_h:
                _____
            tmp.a..([x, max_h])

        _x pre_h 0

        ___ x, height __ tmp:
            __ pre_h > 0
                ans.a..([_x, x, pre_h])

            _x x
            pre_h height

        r.. ans
