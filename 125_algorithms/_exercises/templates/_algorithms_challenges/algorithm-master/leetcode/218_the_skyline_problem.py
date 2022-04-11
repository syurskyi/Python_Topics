"""
REF: https://briangordon.github.io/2014/08/the-skyline-problem.html
"""
_______ heapq


c_ HashHeapq:
    ___ -
        heap    # list
        deleted    # dict

    ___ push  val
        heapq.heappush(heap, val)

    ___ pop
        __ is_empty
            r.. -1

        r.. heapq.heappop(heap)

    ___ remove  val
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
        w.... heap a.. deleted.g.. heap[0]
            val = heapq.heappop(heap)
            deleted[val] -_ 1

        r.. n.. heap


c_ Solution:
    ___ getSkyline  buildings
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
        heap = HashHeapq()

        ___ x, height, is_start __ t__:
            __ is_start:
                heap.push(-height)
            ____
                heap.remove(-height)

            max_h = -heap.top() __ n.. heap.is_empty() ____ 0

            __ ans a.. ans[-1][0] __ x:
                ans.p.. )
            __ ans a.. ans[-1][1] __ max_h:
                _____
            ans.a..([x, max_h])

        r.. ans
