"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ trap(self, A):
        """
        Simplified version of Palantir Technology Online Test 2013

        Algorithm: forward scanning & backward scanning, pointers algorithm
        O(n)
        dp, store the max

        :param A: a list of integers
        :return: an integer
        """
        left_maxs = [0 ___ _ __ A]  # on the left including itself
        right_maxs = [0 ___ _ __ A]  # on the right including itself

        left_max = 0
        ___ ind, val __ e..(A):
            left_max = max(left_max, val)
            left_maxs[ind] = left_max

        right_max = 0
        # for ind, val in enumerate(reversed(A)):  # ind incorrect
        ___ ind, val __ r..(l..(e..(A))):
            right_max = max(right_max, val)
            right_maxs[ind] = right_max

        # calculate the volume
        volume = 0
        ___ ind, val __ e..(A):
            volume += max(0, m..(left_maxs[ind], right_maxs[ind]) - val)

        r.. volume


__ __name____"__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])




