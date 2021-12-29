"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""
from collections import OrderedDict

__author__ = 'Daniel'


class Solution:
    ___ containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        Two Intervals k & t:
        * Use OrderedDict to remember the index and n/t to shrink the interval to -1, 0, 1.
        * In terms of index difference, since there are i-k and i+k, when scanning from left to right, only consider i-k.

        Alternative algorithms:
        Window + TreeSet (Java) / SortedSet (C++)  # TODO

        :type nums: list[int]
        :rtype: bool
        """
        __ k < 1 or t < 0:
            return False

        __ t == 0:
            return self.containsNearByDuplicate(nums, k)

        od = OrderedDict()  # keep the window
        for n in nums:
            key = n/t
            for j in (-1, 0, 1):  # (n-t, n, n+t), shrink the interval
                m = od.get(key+j)
                __ m is not None and abs(m-n) <= t:  # need to recheck, consider case {1, 7}, t=4
                    return True

            while len(od) >= k:
                od.popitem(False)  # not last, i.e. the first

            od[key] = n

        return False

    ___ containsNearByDuplicate(self, nums, k):
        od = OrderedDict()
        for n in nums:
            __ od.get(n):
                return True

            while len(od) >= k:
                od.popitem(False)

            od[n] = n

        return False


__ __name__ == "__main__":
    print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)