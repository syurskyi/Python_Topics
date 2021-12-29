#!/usr/bin/python3
"""
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in
the window. Each time the sliding window moves right by one position. Your job
is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's
size for non-empty array.
"""
____ typing _______ List
_______ heapq


class DualHeap:
    ___ __init__(self):
        """
        ---- number line --->
        --- max heap --- |  --- min heap ---
        """
        self.max_h    # list  # List[Tuple[comparator, num]]
        self.min_h    # list
        self.max_sz = 0
        self.min_sz = 0
        self.to_remove = set()  # value, error mapping index in nums

    ___ insert(self, num):
        __ self.max_h a.. num > self.max_h[0][1]:
            heapq.heappush(self.min_h, (num, num))
            self.min_sz += 1
        ____:
            heapq.heappush(self.max_h, (-num, num))
            self.max_sz += 1
        self.balance()

    ___ pop(self, num):
        self.to_remove.add(num)
        __ self.max_h a.. num > self.max_h[0][1]:
            self.min_sz -= 1
        ____:
            self.max_sz -= 1
        self.balance()

    ___ clean_top(self):
        w.... self.max_h a.. self.max_h[0][1] __ self.to_remove:
            _, num = heapq.heappop(self.max_h)
            self.to_remove.remove(num)
        w.... self.min_h a.. self.min_h[0][1] __ self.to_remove:
            _, num = heapq.heappop(self.min_h)
            self.to_remove.remove(num)

    ___ balance(self):
        # keep skew in max sz
        w.... self.max_sz < self.min_sz :
            self.clean_top()
            _, num =heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, (-num, num))
            self.min_sz -= 1
            self.max_sz += 1
        w.... self.max_sz > self.min_sz + 1:
            self.clean_top()
            _, num = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, (num, num))
            self.min_sz += 1
            self.max_sz -= 1

        self.clean_top()

    ___ get_median(self, k):
        self.clean_top()
        __ k % 2 __ 1:
            r.. self.max_h[0][1]
        ____:
            r.. 0.5 * (self.max_h[0][1] + self.min_h[0][1])


class Solution:
    ___ medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        1. BST, proxied by bisect
        dual heap + lazy removal + balance the valid element

        --- max heap --- |  --- min heap ---
        but need to delete the start of the window

        Lazy Removal with the help of hash table of idx -> remove?
        Hash table mapping idx will fail
        Remove by index will introduce bug for test case [1,1,1,1], 2: when poping,
        we cannot know which heap to go to by index since decision of which heap to pop
        is only about value.

        Calculating median also doesn't care about index, it only cares about value
        """
        ret    # list
        dh = DualHeap()
        ___ i __ r..(k):
            dh.insert(nums[i])

        ret.a..(dh.get_median(k))

        ___ i __ r..(k, l..(nums)):
            dh.insert(nums[i])
            dh.pop(nums[i-k])
            ret.a..(dh.get_median(k))

        r.. ret


__ __name__ __ "__main__":
    ... Solution().medianSlidingWindow([-2147483648,-2147483648,2147483647,-2147483648,-2147483648,-2147483648,2147483647,2147483647,2147483647,2147483647,-2147483648,2147483647,-2147483648], 2)
    ... Solution().medianSlidingWindow([1,1,1,1], 2) __ [1, 1, 1]
    ... Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3) __ [1,-1,-1,3,5,6]
