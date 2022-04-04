#!/usr/bin/python3
"""
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number. The time complexity
must be in O(n).
"""
__author__ = 'Danyang'
_______ heapq


c_ Solution:
    ___ thirdMax  nums
        """
        It is an easy question but error prone:
          1. Choice of min heap or max heap: use min heap (not max heap) because
          we want to know the smallest maximum number
          2. Duplicate number
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. N..

        h    # list
        ___ e __ s..(nums
            __ l..(h) < 3:
                heapq.heappush(h, e)
            ____ l..(h) __ 3 a.. e > h[0]:
                heapq.heappushpop(h, e)

        ... l..(h) <= 3
        __ l..(h) __ 3:
            ret = m..(h)
        ____
            ret = m..(h)
        r.. ret


__ _______ __ _______
    ... Solution().thirdMax([1, 2, 3, 4]) __ 2
    ... Solution().thirdMax([4, 3, 2, 1]) __ 2
    ... Solution().thirdMax([2, 2, 3, 1]) __ 1
    ... Solution().thirdMax([4, 3]) __ 4
