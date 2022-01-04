"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""
____ c.. _______ OrderedDict

__author__ = 'Daniel'


c_ Solution:
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
            r.. F..

        __ t __ 0:
            r.. containsNearByDuplicate(nums, k)

        od = OrderedDict()  # keep the window
        ___ n __ nums:
            key = n/t
            ___ j __ (-1, 0, 1):  # (n-t, n, n+t), shrink the interval
                m = od.get(key+j)
                __ m __ n.. N.. a.. abs(m-n) <= t:  # need to recheck, consider case {1, 7}, t=4
                    r.. T..

            w.... l..(od) >= k:
                od.popitem(F..)  # not last, i.e. the first

            od[key] = n

        r.. F..

    ___ containsNearByDuplicate(self, nums, k):
        od = OrderedDict()
        ___ n __ nums:
            __ od.get(n):
                r.. T..

            w.... l..(od) >= k:
                od.popitem(F..)

            od[n] = n

        r.. F..


__ __name__ __ "__main__":
    print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)