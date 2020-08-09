#!/usr/bin/python3
"""
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number. The time complexity
must be in O(n).
"""
__author__ = 'Danyang'
______ heapq


class Solution:
    ___ thirdMax(self, nums
        """
        It is an easy question but error prone:
          1. Choice of min heap or max heap: use min heap (not max heap) because
          we want to know the smallest maximum number
          2. Duplicate number
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            r_ None

        h = []
        ___ e in set(nums
            __ le.(h) < 3:
                heapq.heappush(h, e)
            ____ le.(h) __ 3 and e > h[0]:
                heapq.heappushpop(h, e)

        assert le.(h) <= 3
        __ le.(h) __ 3:
            ret = min(h)
        ____
            ret = max(h)
        r_ ret


__ __name__ __ "__main__":
    assert Solution().thirdMax([1, 2, 3, 4]) __ 2
    assert Solution().thirdMax([4, 3, 2, 1]) __ 2
    assert Solution().thirdMax([2, 2, 3, 1]) __ 1
    assert Solution().thirdMax([4, 3]) __ 4
