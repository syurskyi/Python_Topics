c_ Solution:
    ___ moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        __ n.. nums:
            r..

        n = l..(nums)
        left = 0

        ___ right __ r..(n):
            __ nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
