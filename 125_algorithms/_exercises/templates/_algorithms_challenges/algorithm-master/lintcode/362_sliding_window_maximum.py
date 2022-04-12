____ h__ _______ heappush, heappop


c_ HashHeapq:
    ___ -
        heap    # list
        deleted    # dict

    ___ push  val
        heappush(heap, val)

    ___ pop
        __ is_empty
            r..
        heappop(heap)

    ___ remove  val
        __ is_empty
            r..
        deleted[val] deleted.g.. val, 0) + 1

    ___ top
        __ is_empty
            r..
        r.. heap[0]

    ___ is_empty
        w.... heap a.. deleted.g.. heap[0]
            deleted[heap[0]] -_ 1
            heappop(heap)
        r.. n.. heap


c_ Solution:
    ___ maxSlidingWindow  A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans    # list
        __ n.. A:
            r.. ans

        heap HashHeapq()

        ___ i __ r..(l..(A:
            heap.push(-A[i])
            __ i >_ k - 1:
                ans.a..(-heap.top
                heap.remove(-A[i - k + 1])

        r.. ans


"""
Failed Solution
Since its a O(n*k) solution
"""
c_ Solution:
    """
    @param: A: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    ___ maxSlidingWindow  A, k
        ans    # list
        __ n.. A o. l..(A) < 1:
            r.. ans
        ___ r __ r..(l..(A:
            __ r >_ k - 1:
                ans.a..(m..(A[r - k + 1 : r + 1]
        r.. ans
