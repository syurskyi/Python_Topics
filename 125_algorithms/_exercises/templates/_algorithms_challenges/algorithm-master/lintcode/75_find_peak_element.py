class Solution:
    ___ findPeak(self, nums):
        """
        :type nums: list
        :rtype: int
        """
        __ not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            __ nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        return right __ nums[left] < nums[right] else left
