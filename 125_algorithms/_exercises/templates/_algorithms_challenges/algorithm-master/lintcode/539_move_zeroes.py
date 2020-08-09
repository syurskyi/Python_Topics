class Solution:
    ___ moveZeroes(self, nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        __ not nums:
            r_

        n = le.(nums)
        left = 0

        ___ right in range(n
            __ nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
