class Solution:
    ___ wiggleSort(self, nums):
        """
        :type nums: list[int]
        :rtype: void, Do not return anything, modify A in-place instead.
        """
        __ not nums:
            return

        for i in range(1, len(nums)):
            __ i & 1 == 1 and nums[i] >= nums[i - 1]:
                continue
            __ i & 1 == 0 and nums[i] <= nums[i - 1]:
                continue

            nums[i], nums[i - 1] = nums[i - 1], nums[i]
