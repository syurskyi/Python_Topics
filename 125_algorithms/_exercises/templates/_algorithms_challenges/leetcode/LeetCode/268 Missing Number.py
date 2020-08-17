"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
complexity?
"""
__author__ = 'Daniel'


class Solution(object
    ___ missingNumber(self, nums
        """
        Algorithm:
        Hashmap, but to save space, use the array itself as the hashmap

        Notice:
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        Above is wrong, since evaluate from left to right; thus, when nums[nums[i]] on RHS is None, on LHS, nums[i] is
        eval to None and nums[nums[i]] indexes by None, causing errors.

        Alternatively, it is correct that:
            nums[nums[i]], nums[i]= nums[i], nums[nums[i]]

        To be safe, just use:
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]

        :type nums: List[int]
        :rtype: int
        """
        num_n = None
        n = le.(nums)

        i = 0
        w___ i < n:
            __ nums[i] __ n:
                num_n = nums[i]
                nums[i] = None
                i += 1

            ____ nums[i] pa__ not None and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]

            ____
                i += 1

        __ not num_n:
            r_ n

        r_ nums.index(None)


__ __name__ __ "__main__":
    assert Solution().missingNumber([2, 0]) __ 1
