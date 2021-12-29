"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""
____ collections _______ OrderedDict

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
        __ k < 1 o. t < 0:
            r.. False

        __ t __ 0:
            r.. self.containsNearByDuplicate(nums, k)

        od = OrderedDict()  # keep the window
        ___ n __ nums:
            key = n/t
            ___ j __ (-1, 0, 1):  # (n-t, n, n+t), shrink the interval
                m = od.get(key+j)
                __ m __ n.. N.. and abs(m-n) <= t:  # need to recheck, consider case {1, 7}, t=4
                    r.. True

            while l..(od) >= k:
                od.popitem(False)  # not last, i.e. the first

            od[key] = n

        r.. False

    ___ containsNearByDuplicate(self, nums, k):
        od = OrderedDict()
        ___ n __ nums:
            __ od.get(n):
                r.. True

            while l..(od) >= k:
                od.popitem(False)

            od[n] = n

        r.. False


__ __name__ __ "__main__":
    print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)