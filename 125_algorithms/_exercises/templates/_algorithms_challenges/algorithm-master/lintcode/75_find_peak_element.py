class Solution:
    ___ findPeak(self, nums
        """
        :type nums: list
        :rtype: int
        """
        __ not nums:
            r_ -1

        left, right = 0, le.(nums) - 1

        w___ left + 1 < right:
            mid = (left + right) // 2

            __ nums[mid] < nums[mid + 1]:
                left = mid
            ____
                right = mid

        r_ right __ nums[left] < nums[right] else left
