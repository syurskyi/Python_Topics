class Solution:
    ___ wiggleSort(self, nums):
        """
        :type nums: list[int]
        :rtype: void, Do not return anything, modify A in-place instead.
        """
        __ n.. nums:
            r..

        ___ i __ r..(1, l..(nums)):
            __ i & 1 __ 1 and nums[i] >= nums[i - 1]:
                continue
            __ i & 1 __ 0 and nums[i] <= nums[i - 1]:
                continue

            nums[i], nums[i - 1] = nums[i - 1], nums[i]
