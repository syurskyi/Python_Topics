from heapq ______ heappush, heappop


class HashHeapq:
    ___ __init__(self
        self.heap = []
        self.deleted = {}

    ___ push(self, val
        heappush(self.heap, val)

    ___ pop(self
        __ self.is_empty(
            r_
        heappop(self.heap)

    ___ remove(self, val
        __ self.is_empty(
            r_
        self.deleted[val] = self.deleted.get(val, 0) + 1

    ___ top(self
        __ self.is_empty(
            r_
        r_ self.heap[0]

    ___ is_empty(self
        w___ self.heap and self.deleted.get(self.heap[0]
            self.deleted[self.heap[0]] -= 1
            heappop(self.heap)
        r_ not self.heap


class Solution:
    ___ maxSlidingWindow(self, A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        __ not A:
            r_ ans

        heap = HashHeapq()

        for i in range(le.(A)):
            heap.push(-A[i])
            __ i >= k - 1:
                ans.append(-heap.top())
                heap.remove(-A[i - k + 1])

        r_ ans


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
    ___ maxSlidingWindow(self, A, k
        ans = []
        __ not A or le.(A) < 1:
            r_ ans
        for r in range(le.(A)):
            __ r >= k - 1:
                ans.append(max(A[r - k + 1 : r + 1]))
        r_ ans
