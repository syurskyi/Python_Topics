"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume
that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
_______ r__

__author__ = 'Daniel'


c_ Solution(o..
    ___ - , nums
        """
        :type nums: List[int]
        """
        A = nums

    ___ pick  target
        """
        O(n)
        Reservoir Sampling
        :type target: int
        :rtype: int
        """
        sz = 0
        ret = N..
        ___ idx, val __ e..(A
            __ val __ target:
                sz += 1
                p = r__.randrange(0, sz)
                __ p __ 0:
                    ret = idx

        r.. ret


c_ SolutionError(o..
    ___ - , nums
        """
        Reservoir Sampling
        Assume pick is only called once
        :type nums: List[int]
        """
        d    # dict
        ___ idx, val __ e..(nums
            __ val n.. __ d:
                d[val] = (idx, 1)
            ____
                prev, sz = d[val]
                p = r__.randrange(0, sz)
                __ p < sz:
                    d[val] = (idx, sz + 1)
                ____
                    d[val] = (prev, sz + 1)

    ___ pick  target
        """
        :type target: int
        :rtype: int
        """
        r.. d[target][0]