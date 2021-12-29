____ heapq _______ heappush, heappop


class HashHeapq:
    ___ __init__(self):
        self.heap    # list
        self.deleted = {}

    ___ push(self, val):
        heappush(self.heap, val)

    ___ pop(self):
        __ self.is_empty():
            r..
        heappop(self.heap)

    ___ remove(self, val):
        __ self.is_empty():
            r..
        self.deleted[val] = self.deleted.get(val, 0) + 1

    ___ top(self):
        __ self.is_empty():
            r..
        r.. self.heap[0]

    ___ is_empty(self):
        w.... self.heap a.. self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1
            heappop(self.heap)
        r.. n.. self.heap


class Solution:
    ___ maxSlidingWindow(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans    # list
        __ n.. A:
            r.. ans

        heap = HashHeapq()

        ___ i __ r..(l..(A)):
            heap.push(-A[i])
            __ i >= k - 1:
                ans.a..(-heap.top())
                heap.remove(-A[i - k + 1])

        r.. ans


"""
Failed Solution
Since its a O(n*k) solution
"""
class Solution:
    """
    @param: A: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    ___ maxSlidingWindow(self, A, k):
        ans    # list
        __ n.. A o. l..(A) < 1:
            r.. ans
        ___ r __ r..(l..(A)):
            __ r >= k - 1:
                ans.a..(max(A[r - k + 1 : r + 1]))
        r.. ans
