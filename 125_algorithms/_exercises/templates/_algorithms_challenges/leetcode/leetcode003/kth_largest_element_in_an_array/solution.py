"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length
"""

_______ heapq

c_ Solution(o..
    ___ findKthLargest  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h    # list
        ___ e __ nums:
            heapq.heappush(h, (-e, e
        ___ i __ r..(k
            w, e = heapq.heappop(h)
            __ i __ k - 1:
                r.. e


a1 = [3, 2, 1, 5, 6, 4]
s = Solution()
res = s.findKthLargest(a1, 2)
print(res)
